import csv, json
from collections import Counter
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / "data" / "events.csv").open() as f:
    rows = list(csv.DictReader(f))
ids = Counter(r["record_id"] for r in rows)
max_loaded = max(date.fromisoformat(r["loaded_at"]) for r in rows)
checks = [
    {"name": "record_id_unique", "status": "passed" if all(v == 1 for v in ids.values()) else "failed", "failures": sum(v - 1 for v in ids.values() if v > 1)},
    {"name": "account_id_not_null", "status": "passed" if all(r["account_id"] for r in rows) else "failed", "failures": sum(1 for r in rows if not r["account_id"])},
    {"name": "event_count_non_negative", "status": "passed" if all(int(r["event_count"]) >= 0 for r in rows) else "failed", "failures": sum(1 for r in rows if int(r["event_count"]) < 0)},
    {"name": "freshness_within_2_days", "status": "passed" if (date(2026, 8, 25) - max_loaded).days <= 2 else "failed", "failures": 0},
]
(root / "outputs").mkdir(exist_ok=True)
with (root / "outputs" / "quality_report.json").open("w") as f:
    json.dump({"checks": checks}, f, indent=2)
print(json.dumps({"checks": checks}, indent=2))
