# Customer 360 Analytics Platform

> Portfolio recreation using synthetic data. Inspired by real senior data engineering patterns, but it contains no employer code, schemas, credentials, or confidential data.

## What This Demonstrates
A modular CRM analytics warehouse with synthetic companies, contacts, deals, and support tickets. The project demonstrates reusable customer models, business-ready marts, and documentation patterns for self-service analytics.

## Architecture
Raw CRM entities feed a curated customer mart that standardizes company, revenue, contact, and support indicators.

## LinkedIn Summary
Designed a modular Customer 360 analytics foundation covering contacts, companies, deals, support tickets, product usage, and lifecycle signals.

## Run
`python3 run_pipeline.py` regenerates the customer mart from synthetic data.

## Case Study Detail

This project is modeled after a common enterprise analytics problem: CRM objects are technically related, but the logic needed to answer business questions is scattered across analysts, dashboards, and duplicated SQL. The portfolio version keeps the domain public-safe while preserving the engineering pattern.

The pipeline starts with companies, contacts, deals, and support tickets. It then creates a customer-level mart that can answer practical questions such as which companies have active support issues, where closed-won revenue exists, and how contact coverage varies by customer.

Production equivalent patterns:

- dbt models for staging, intermediate, and mart layers
- Snowflake or BigQuery warehouse tables
- data tests for primary keys, foreign keys, duplicate records, and freshness
- business glossary fields for ownership, refresh cadence, and metric definition
- dashboard-ready customer dimensions for analysts and customer teams

Reviewer signal:

This project shows that I understand how to turn messy business entities into reusable analytics infrastructure, not just write isolated SQL queries.
