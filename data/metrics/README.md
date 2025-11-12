# Metrics

Track trends, not people. Use the CSV files here to plot throughput,
MTTR, papercuts removed, buffer health, and near-misses addressed.

## Workflow

1. After every repair session, append a new row to `metrics-dashboard.csv`
   with the week number, tickets closed, MTTR (in hours), papercuts burned
   down, buffer hours, and any near-misses.
2. Cross-link the row to the matching session notes and retro so future
   humans can chase context.
3. Review these numbers during the retro to decide the next systemic fix.

> Pro tip: if spreadsheets are your jam, import this CSV into your tracker
> of choice, but keep this canonical copy up to date in the repo.
