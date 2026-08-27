import csv
from pathlib import Path

root = Path(__file__).resolve().parent
rows = []
with (root / "data" / "account_signals.csv").open() as f:
    for row in csv.DictReader(f):
        usage = int(row["weekly_active_users"])
        tickets = int(row["open_support_tickets"])
        csat = float(row["avg_csat"])
        renewal_days = int(row["days_to_renewal"])
        score = max(0, min(100, int(usage / 12 + csat * 12 - tickets * 5 + min(20, renewal_days / 9))))
        row["health_score"] = score
        row["segment"] = "at_risk" if score < 45 else "watch" if score < 70 else "healthy"
        rows.append(row)

out = root / "outputs" / "daily_account_health_scores.csv"
out.parent.mkdir(exist_ok=True)
with out.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {out}")
