import csv
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent

def load(name):
    with (root / "data" / name).open() as f:
        return list(csv.DictReader(f))

companies = load("companies.csv")
contacts = load("contacts.csv")
deals = load("deals.csv")
tickets = load("tickets.csv")

won_by_company = defaultdict(int)
open_tickets = Counter()
contacts_by_company = Counter()

for row in deals:
    if row["stage"] == "closed_won":
        won_by_company[row["company_id"]] += int(row["amount_usd"])
for row in tickets:
    if row["status"] != "closed":
        open_tickets[row["company_id"]] += 1
for row in contacts:
    contacts_by_company[row["company_id"]] += 1

out = root / "outputs" / "customer_360_mart.csv"
out.parent.mkdir(exist_ok=True)
with out.open("w", newline="") as f:
    fieldnames = ["company_id", "company_name", "industry", "contacts", "open_tickets", "closed_won_revenue_usd"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for co in companies:
        cid = co["company_id"]
        writer.writerow({
            "company_id": cid,
            "company_name": co["company_name"],
            "industry": co["industry"],
            "contacts": contacts_by_company[cid],
            "open_tickets": open_tickets[cid],
            "closed_won_revenue_usd": won_by_company[cid],
        })
print(f"Wrote {out}")
