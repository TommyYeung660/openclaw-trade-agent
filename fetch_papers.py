#!/usr/bin/env python3
"""Simple arXiv paper fetcher for morning briefing"""
import httpx
import feedparser
from datetime import datetime, timedelta, timezone

CATEGORIES = [
    "q-fin.TR",
    "q-fin.RM",
    "q-fin.ST",
    "q-fin.PM",
    "cs.LG",
    "stat.ML"
]

def fetch_arxiv(category, max_results=10):
    """Fetch recent papers from arXiv RSS"""
    rss_url = f"https://export.arxiv.org/rss/{category}"
    try:
        resp = httpx.get(rss_url, timeout=30)
        if resp.status_code != 200:
            return []
        feed = feedparser.parse(resp.text)
        papers = []
        for entry in feed.entries[:max_results]:
            # Extract arxiv_id from link
            link = entry.get('link', '')
            arxiv_id = link.split('/')[-1] if link else ''

            papers = papers + [{
                'arxiv_id': arxiv_id,
                'title': entry.get('title', ''),
                'summary': entry.get('summary', ''),
                'link': link,
                'published': entry.get('published', ''),
                'authors': [a.get('name', '') for a in entry.get('authors', [])],
                'category': category
            }]
        return papers
    except Exception as e:
        print(f"Error fetching {category}: {e}")
        return []

def main():
    all_papers = []
    for cat in CATEGORIES:
        print(f"Fetching {cat}...")
        papers = fetch_arxiv(cat, max_results=5)
        all_papers.extend(papers)
        print(f"  Found {len(papers)} papers")

    # Print papers in a format easy to copy
    for p in all_papers:
        print(f"\n{'='*80}")
        print(f"ID: {p['arxiv_id']}")
        print(f"Title: {p['title']}")
        print(f"Category: {p['category']}")
        print(f"Authors: {', '.join(p['authors'][:3])}")
        print(f"Link: {p['link']}")
        print(f"Summary: {p['summary'][:500]}..." if len(p['summary']) > 500 else f"Summary: {p['summary']}")

if __name__ == "__main__":
    main()
