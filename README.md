# Football-Analytics

A learning project to build coding and Git/GitHub fluency using football data analytics.

## What this does

Analyzes Brazilian Série A match data to calculate what percentage of each
current Série A team's matches go over 2.5 total goals, using historical
data from 2003-2024.

## Files

- `analyze_goals.py` — main script: loads match data, filters to current
  Série A teams, calculates over/under 2.5 goal rates with sample sizes,
  and generates a bar chart
- `campeonato-brasileiro-full.csv` — match data source (2003-2024)
- `test_api.py` — proof-of-concept script for pulling live data via the
  API-Football API (see limitation below)

## Known limitation

The free tier of API-Football only allows access to the 2022-2024 seasons,
so this project cannot currently pull 2025-2026 match results. The static
CSV (through 2024) is the most current data available without a paid API
plan. Upgrading this is a clear next step.

## Run it

Requires `pandas` and `matplotlib` (`pip3 install pandas matplotlib`).