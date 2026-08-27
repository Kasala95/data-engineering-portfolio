# Ocholi Idakwo - Senior Data Engineering Portfolio

This repository contains six public-safe, end-to-end data engineering portfolio projects built with synthetic data. The projects are designed to demonstrate senior-level thinking across analytics engineering, cloud data platforms, revenue data, data governance, observability, and healthcare machine learning workflows.

Live portfolio site: https://kasala95.github.io/data-engineering-portfolio/

## Why This Portfolio Exists

Most data engineering work cannot be published directly because it involves employer systems, customer records, proprietary schemas, regulated data, internal dashboards, or private infrastructure. This portfolio recreates the shape of that work with synthetic data so it can be reviewed publicly without exposing confidential information.

Each project includes:

- Synthetic source data
- A runnable Python pipeline or validation script
- Generated output artifacts
- Recruiter-readable case-study documentation
- A public project page for LinkedIn Featured and Projects sections

## Portfolio Projects

| Project | Focus Area | Public Artifacts |
| --- | --- | --- |
| [Customer 360 Analytics Platform](projects/customer-360-analytics-platform) | CRM modeling, customer marts, self-service analytics | Synthetic CRM data, SQL model, customer mart |
| [SaaS Account Health Scoring](projects/saas-account-health-scoring) | Customer success analytics, feature engineering, operational scoring | Account signals, scoring script, health output |
| [Revenue Source Of Truth Model](projects/revenue-source-of-truth-model) | Finance data controls, FX conversion, reconciliation | Deal data, FX rates, recognized revenue, reconciliation report |
| [Data Quality And Observability Framework](projects/data-quality-observability-framework) | Data quality checks, freshness, incident-ready reporting | Event data, validation script, JSON quality report |
| [Healthcare Readmission Risk Pipeline](projects/healthcare-readmission-risk-pipeline) | Healthcare analytics, batch ML scoring, risk bands | Synthetic patient data, risk scoring script, output scores |
| [Clinical Notes NLP Code Detection](projects/clinical-notes-nlp-code-detection) | Clinical NLP, review queues, compliance-aware workflow design | Synthetic notes, detection script, candidate-code findings |

## Senior Data Engineering Themes

### Data Modeling And Analytics Engineering

The Customer 360 and metric marts show how raw business entities can become documented, reusable, analysis-ready models. The emphasis is on clean joins, repeatable transformation logic, ownership, and stakeholder-ready outputs.

### Operational Data Products

The account health scoring project demonstrates how warehouse data becomes operational intelligence. The output is designed for CRM enrichment, customer success prioritization, and daily business workflows.

### Revenue Data Trust

The revenue source-of-truth project focuses on the controls that make financial reporting trustworthy: close status rules, deal-level deduplication, currency conversion, and reconciliation outputs.

### Governance And Observability

The observability project demonstrates how automated checks can detect duplicate records, missing business keys, invalid values, and freshness issues before data is published.

### Healthcare And ML Data Engineering

The healthcare projects show experience with regulated-domain thinking, feature engineering, batch scoring, clinical-style text processing, and human-review workflows without using protected health information.

## Run The Projects

Each project uses only the Python standard library.

```bash
cd projects/customer-360-analytics-platform
python3 run_pipeline.py
```

```bash
cd projects/saas-account-health-scoring
python3 score_accounts.py
```

```bash
cd projects/revenue-source-of-truth-model
python3 reconcile_revenue.py
```

```bash
cd projects/data-quality-observability-framework
python3 validate_events.py
```

```bash
cd projects/healthcare-readmission-risk-pipeline
python3 score_readmission_risk.py
```

```bash
cd projects/clinical-notes-nlp-code-detection
python3 detect_candidate_codes.py
```

## Public Data Disclaimer

All datasets are synthetic. This repository does not contain employer code, employer schemas, customer data, patient data, credentials, production architecture, or confidential business logic.

## Suggested LinkedIn Use

Add the live site to Featured, then add each project under the LinkedIn Projects section. Use `linkedin-project-copy.md` for polished copy that can be pasted into LinkedIn.
