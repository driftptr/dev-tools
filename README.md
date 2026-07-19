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
| `url_ping.py` | Quick HTTP GET/HEAD reachability check |

## Usage

```bash
python3 json_pretty.py payload.json
python3 env_check.py DATABASE_URL API_KEY
python3 csv_merge.py left.csv right.csv --key id
python3 csv_merge.py left.tsv right.tsv --key id --delimiter '\t'
tail -f app.log | python3 log_tail_filter.py "ERROR|WARN" -n
tail -f app.log | python3 log_tail_filter.py "DEBUG" -v
python3 sync_paths.py
python3 url_ping.py https://api.example.com/health --head --timeout 5 --retries 2
```

These are quick personal tools, not production code.

---

*driftptr*
