"""Sync factor hypotheses to Dropbox for qlib_rd_agent consumption.

Reads daily YAML files from outputs/factor_hypotheses/,
merges them into an aggregated file, and uploads to Dropbox.

Usage:
    python scripts/sync_hypotheses_to_dropbox.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import dropbox
import yaml

# Paths
WORKSPACE = Path(__file__).resolve().parent.parent
HYPOTHESES_DIR = WORKSPACE / "outputs" / "factor_hypotheses"
SYNC_STATE_FILE = HYPOTHESES_DIR / ".sync_state.json"
AGGREGATED_FILE = HYPOTHESES_DIR / "aggregated_hypotheses.yaml"
SCANNER_ENV = WORKSPACE / "qlib_market_scanner" / ".env"

# Dropbox target
DROPBOX_UPLOAD_PATH = "/qlib_shared/rdagent_inputs/hypotheses/aggregated_hypotheses.yaml"

# Retention: keep hypotheses from the last N days
RETENTION_DAYS = 30

HKT = timezone(timedelta(hours=8))


def load_dropbox_credentials() -> dict[str, str]:
    """Load Dropbox credentials from qlib_market_scanner .env."""
    creds: dict[str, str] = {}
    if not SCANNER_ENV.exists():
        raise FileNotFoundError(f"Scanner .env not found: {SCANNER_ENV}")

    for line in SCANNER_ENV.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("'\"")
            if key.startswith("DROPBOX_"):
                creds[key] = value
    return creds


def get_dropbox_client(creds: dict[str, str]) -> dropbox.Dropbox:
    """Create Dropbox client using refresh token."""
    return dropbox.Dropbox(
        oauth2_refresh_token=creds["DROPBOX_REFRESH_TOKEN"],
        app_key=creds["DROPBOX_APP_KEY"],
        app_secret=creds["DROPBOX_APP_SECRET"],
    )


def load_sync_state() -> dict:
    """Load sync state (last synced files and timestamps)."""
    if SYNC_STATE_FILE.exists():
        return json.loads(SYNC_STATE_FILE.read_text())
    return {"last_sync": None, "synced_files": []}


def save_sync_state(state: dict) -> None:
    """Persist sync state."""
    SYNC_STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def collect_daily_hypotheses() -> list[dict]:
    """Collect all hypotheses from daily YAML files within retention window."""
    cutoff = datetime.now(HKT) - timedelta(days=RETENTION_DAYS)
    all_hypotheses: list[dict] = []
    seen_ids: set[str] = set()

    yaml_files = sorted(HYPOTHESES_DIR.glob("????-??-??.yaml"))

    for fp in yaml_files:
        # Parse date from filename
        try:
            file_date = datetime.strptime(fp.stem, "%Y-%m-%d").replace(tzinfo=HKT)
        except ValueError:
            continue

        if file_date < cutoff:
            continue

        try:
            data = yaml.safe_load(fp.read_text())
        except Exception as e:
            print(f"[WARN] Failed to parse {fp.name}: {e}", file=sys.stderr)
            continue

        if not data or "hypotheses" not in data:
            continue

        for h in data["hypotheses"]:
            h_id = h.get("id", "")
            if h_id and h_id not in seen_ids:
                seen_ids.add(h_id)
                all_hypotheses.append(h)

    return all_hypotheses


def build_aggregated(hypotheses: list[dict]) -> dict:
    """Build aggregated YAML structure."""
    return {
        "version": "1.0",
        "generated_at": datetime.now(HKT).isoformat(),
        "source_agent": "trade-agent",
        "total_count": len(hypotheses),
        "hypotheses": hypotheses,
    }


def upload_to_dropbox(dbx: dropbox.Dropbox, content: bytes, path: str) -> None:
    """Upload content to Dropbox, overwriting if exists."""
    dbx.files_upload(
        content,
        path,
        mode=dropbox.files.WriteMode.overwrite,
    )
    print(f"[OK] Uploaded to Dropbox: {path}")


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    # 1. Collect hypotheses
    hypotheses = collect_daily_hypotheses()
    if not hypotheses:
        print("[INFO] No hypotheses found to sync. Exiting.")
        return

    print(f"[INFO] Collected {len(hypotheses)} hypotheses from daily files.")

    # 2. Build aggregated YAML
    aggregated = build_aggregated(hypotheses)
    yaml_content = yaml.dump(
        aggregated,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )

    # 3. Write local aggregated file
    AGGREGATED_FILE.write_text(yaml_content)
    print(f"[OK] Written aggregated file: {AGGREGATED_FILE}")

    if dry_run:
        print("[DRY-RUN] Skipping Dropbox upload.")
        return

    # 4. Upload to Dropbox
    try:
        creds = load_dropbox_credentials()
        dbx = get_dropbox_client(creds)

        # Ensure parent folder exists
        try:
            dbx.files_create_folder_v2("/qlib_shared/rdagent_inputs/hypotheses")
        except dropbox.exceptions.ApiError:
            pass  # Folder already exists

        upload_to_dropbox(dbx, yaml_content.encode("utf-8"), DROPBOX_UPLOAD_PATH)
    except Exception as e:
        print(f"[ERROR] Dropbox upload failed: {e}", file=sys.stderr)
        sys.exit(1)

    # 5. Update sync state
    state = load_sync_state()
    state["last_sync"] = datetime.now(HKT).isoformat()
    state["synced_files"] = [f.name for f in sorted(HYPOTHESES_DIR.glob("????-??-??.yaml"))]
    state["total_hypotheses"] = len(hypotheses)
    save_sync_state(state)
    print(f"[OK] Sync state updated.")


if __name__ == "__main__":
    main()
