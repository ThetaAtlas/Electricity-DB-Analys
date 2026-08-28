U.S. Energy Inflation Genie Project

This folder contains the Databricks notebooks used to build a small data product that analyzes U.S. electricity prices, inflation, and natural gas prices using FRED data.

Notebook Order

Run the notebooks in this order:

01_ingest_fred_bronze.py
Pulls the configured FRED series from the API and writes the raw observations to a Unity Catalog Delta table.

02_transform_fred_silver.sql
Cleans and standardizes the raw FRED observations into a typed Silver table.

03_build_energy_inflation_gold.sql
Builds the business-facing monthly Gold table and calculates inflation, spreads, and rolling correlation metrics.

04_create_energy_inflation_metric_view.sql
Creates the Unity Catalog metric view used as the governed semantic layer for Genie.

05_create_genie_agent.py
Creates or updates the Genie Agent and connects it to the metric view.

Data Sources

APU000072610 — Average U.S. electricity price

CUSR0000SEHF01 — Electricity CPI

CPIAUCSL — Headline CPI

CPILFESL — Core CPI

MHHNGSP — Henry Hub natural gas spot price

Setup

Before running the notebooks:

Create a Databricks secret scope containing the FRED API key.

Update the catalog and schema names if needed.

Ensure the target Unity Catalog schema exists.

Provide a Pro or Serverless SQL Warehouse ID for the Genie Agent notebook.

Ensure the user running the notebooks has the required Unity Catalog and Genie permissions.

Architecture

FRED API
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Metric View
   ↓
Genie Agent

The project is intentionally small and focused so the full pipeline can be understood, tested, and demonstrated end to end.