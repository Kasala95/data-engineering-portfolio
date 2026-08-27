import csv, json
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / "data" / "fx_rates.csv").open() as f:
    rates = {r["currency"]: float(r["rate_to_usd"]) for r in csv.DictReader(f)}

recognized = []
seen = set()
with (root / "data" / "deals.csv").open() as f:
    for row in csv.DictReader(f):
        if row["status"] != "closed_won" or row["deal_id"] in seen:
            continue
        seen.add(row["deal_id"])
        row["amount_usd"] = round(float(row["amount_native"]) * rates[row["currency"]], 2)
        recognized.append(row)

(root / "outputs").mkdir(exist_ok=True)
with (root / "outputs" / "recognized_revenue.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=recognized[0].keys())
    writer.writeheader()
    writer.writerows(recognized)
with (root / "outputs" / "reconciliation_report.json").open("w") as f:
    json.dump({"closed_won_deals": len(recognized), "recognized_revenue_usd": round(sum(r["amount_usd"] for r in recognized), 2)}, f, indent=2)
print("Revenue reconciliation complete")
