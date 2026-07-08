# dev-tools

Collection of small utility scripts I use for day-to-day dev work.

## Tools

| Script | Description |
|--------|-------------|
| `json_pretty.py` | Pretty-print JSON from file or stdin |
| `env_check.py` | Fail if required environment variables are missing |
| `csv_merge.py` | Merge two CSV files on a key column |
| `log_tail_filter.py` | Filter log lines with a regex |
| `sync_paths.py` | Resolve local project paths |

## Usage

```bash
python3 json_pretty.py payload.json
python3 env_check.py DATABASE_URL API_KEY
python3 csv_merge.py left.csv right.csv --key id
tail -f app.log | python3 log_tail_filter.py "ERROR|WARN"
python3 sync_paths.py
```

These are quick personal tools, not production code.

---

*driftptr*
