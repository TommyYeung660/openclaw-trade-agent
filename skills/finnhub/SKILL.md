---
name: finnhub
description: Access Finnhub API for real-time stock quotes, company news, market data, financial statements, and trading signals. Use when you need current stock prices, company news, earnings data, or market analysis.
homepage: https://finnhub.io
---

# Finnhub API

Access real-time and historical stock market data, company news, financial statements, and market indicators via the Finnhub API.

## IMPORTANT: Usage Restrictions

**This skill is for the agent's own learning and research ONLY.**
- Use Finnhub data to enrich your daily learning, market analysis, and knowledge building.
- You may propose improvements to managed projects based on insights gained.
- **You MUST NOT directly modify any project code or data pipelines to integrate Finnhub.**
- **You MUST NOT replace or alter existing data sources in any managed project.**
- All project changes must be presented as "suggestions" for human review.

## Quick Start

API key is provided via environment variable `FINNHUB_API_KEY`.

## API Endpoints

Base URL: `https://finnhub.io/api/v1`

All requests require `?token=${FINNHUB_API_KEY}` parameter.

### Stock Quotes (Real-time)

```bash
curl "https://finnhub.io/api/v1/quote?symbol=AAPL&token=${FINNHUB_API_KEY}"
```

Returns: `c` (current price), `h` (high), `l` (low), `o` (open), `pc` (previous close), `t` (timestamp)

### Company News

```bash
curl "https://finnhub.io/api/v1/company-news?symbol=AAPL&from=2025-01-01&to=2025-02-01&token=${FINNHUB_API_KEY}"
curl "https://finnhub.io/api/v1/news?category=general&token=${FINNHUB_API_KEY}"
```

### Company Profile

```bash
curl "https://finnhub.io/api/v1/stock/profile2?symbol=AAPL&token=${FINNHUB_API_KEY}"
```

### Financial Statements

```bash
# Income statement
curl "https://finnhub.io/api/v1/stock/financials-reported?symbol=AAPL&token=${FINNHUB_API_KEY}"

# Balance sheet
curl "https://finnhub.io/api/v1/stock/financials-reported?symbol=AAPL&statement=bs&token=${FINNHUB_API_KEY}"

# Cash flow
curl "https://finnhub.io/api/v1/stock/financials-reported?symbol=AAPL&statement=cf&token=${FINNHUB_API_KEY}"
```

### Market Data

```bash
# Stock candles (OHLCV)
curl "https://finnhub.io/api/v1/stock/candle?symbol=AAPL&resolution=D&from=1609459200&to=1640995200&token=${FINNHUB_API_KEY}"

# Stock symbols (search)
curl "https://finnhub.io/api/v1/search?q=apple&token=${FINNHUB_API_KEY}"

# Market status
curl "https://finnhub.io/api/v1/stock/market-status?exchange=US&token=${FINNHUB_API_KEY}"
```

### Earnings & Calendar

```bash
curl "https://finnhub.io/api/v1/calendar/earnings?from=2025-02-01&to=2025-02-28&token=${FINNHUB_API_KEY}"
curl "https://finnhub.io/api/v1/stock/earnings?symbol=AAPL&token=${FINNHUB_API_KEY}"
```

## Rate Limits

Free tier: 60 API calls/minute.

## Notes

- Always include `token=${FINNHUB_API_KEY}` in query parameters
- Date format: `YYYY-MM-DD`
- Timestamps: Unix epoch seconds
- Symbol format: use exchange prefix if needed (e.g., `US:AAPL`)
