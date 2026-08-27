# SaaS Account Health Scoring

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A synthetic customer success scoring pipeline that combines usage, support, satisfaction, renewal timing, and account value into operational health segments.

## Scoring Logic
The score favors active usage and high CSAT, penalizes support burden, and considers renewal urgency.

## LinkedIn Summary
Built a daily account health scoring system for customer retention, expansion, and proactive support prioritization.

## Run
`python3 score_accounts.py` creates account health outputs.

## Case Study Detail

This project demonstrates an operational analytics pattern: converting customer behavior into a score that teams can act on every day. The synthetic dataset combines usage, support tickets, CSAT, renewal timing, and ARR to produce a health score and account segment.

The score is intentionally transparent. In production, explainability matters because customer-facing teams need to understand why an account moved from healthy to watch or at risk. This is closer to a practical data product than a black-box model.

Production equivalent patterns:

- scheduled feature pipelines in Databricks, Airflow, or cloud-native orchestration
- feature checks for missing usage, ticket spikes, stale CSAT, and renewal-date anomalies
- CRM-ready output tables for reverse ETL
- monitoring for score distribution shifts and upstream data outages
- stakeholder review with Customer Success, Sales, Support, and Finance

Reviewer signal:

This project shows how I design data products that move beyond dashboards and into daily business workflows.
