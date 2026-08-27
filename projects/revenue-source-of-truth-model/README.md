# Revenue Source Of Truth Model

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A synthetic finance analytics project that standardizes revenue recognition logic, currency conversion, and reconciliation controls.

## Controls
The pipeline enforces closed-won filtering, standardized FX rates, and deal-level output checks.

## LinkedIn Summary
Created a unified revenue model to align Finance, Marketing, and executive reporting around consistent revenue definitions.

## Run
`python3 reconcile_revenue.py` produces recognized revenue and a reconciliation report.

## Case Study Detail

This project demonstrates how revenue analytics needs engineering controls, not just aggregation. A trusted revenue model has to define which deals count, how currencies are converted, how duplicates are handled, and how discrepancies are surfaced before reporting.

The synthetic pipeline filters closed-won deals, applies standardized exchange rates, writes recognized revenue output, and generates a reconciliation report. In a real environment, this same pattern supports Finance, Marketing, Sales Operations, and executive reporting.

Production equivalent patterns:

- Snowflake models for bookings, pipeline, recognized revenue, and attribution
- controlled FX rate reference tables
- reconciliation thresholds before dashboard publication
- ownership and sign-off workflows for metric definition changes
- audit-friendly output for quarterly reporting cycles

Reviewer signal:

This project shows I can work where data engineering meets financial trust, stakeholder alignment, and business-critical reporting.
