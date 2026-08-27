import csv, math
from pathlib import Path

root = Path(__file__).resolve().parent
scored = []
with (root / "data" / "synthetic_patients.csv").open() as f:
    for row in csv.DictReader(f):
        z = -4 + int(row["age"]) * 0.025 + int(row["prior_admissions"]) * 0.38 + int(row["abnormal_lab_count"]) * 0.22 + int(row["medication_count"]) * 0.06 + int(row["social_risk_flag"]) * 0.65
        risk = round(1 / (1 + math.exp(-z)), 3)
        row["readmission_risk"] = risk
        row["risk_band"] = "high" if risk >= .55 else "medium" if risk >= .3 else "low"
        scored.append(row)
(root / "outputs").mkdir(exist_ok=True)
with (root / "outputs" / "daily_readmission_scores.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=scored[0].keys())
    writer.writeheader()
    writer.writerows(scored)
print("Generated readmission scores")
