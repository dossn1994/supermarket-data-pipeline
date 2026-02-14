# 🛒 Supermarket Sales Data Pipeline

## 📌 Project Overview

This project demonstrates the design and implementation of an end-to-end
data pipeline that:

-   Extracts sales data programmatically from Kaggle using the Kaggle API
-   Transforms it into dimensional (star schema) format
-   Loads it into a SQLite database
-   Generates an analytical report using SQL (with joins and window functions)
-   Proposes a scalable cloud deployment architecture (GCP)

------------------------------------------------------------------------

# 🏗️ Architecture Overview (Local Implementation)

Kaggle API
→ Python Extraction Script
→ Transformation (Star Schema)
→ SQLite Database
→ SQL Analytical Report

------------------------------------------------------------------------

# 📊 Data Modeling

## Dimension Tables

### dim_customer

-   customer_id (PK)
-   customer_type
-   gender

### dim_product

-   product_id (PK)
-   product_line
-   unit_price

## Fact Table

### fact_sales

-   sale_id (PK)
-   invoice_id
-   branch
-   city
-   date
-   time
-   payment
-   quantity
-   tax
-   sales
-   cogs
-   gross_income
-   rating
-   customer_id (FK)
-   product_id (FK)

------------------------------------------------------------------------

# 🚀 Setup Instructions

## 1️⃣ Clone Repository

git clone https://github.com/dossn1994/supermarket-data-pipeline.git\
cd supermarket-data-pipeline

## 2️⃣ Install Requirements

pip install pandas kaggle

## 3️⃣ Configure Kaggle API

- Go to Kaggle → Account → Create API Token
- Move kaggle.json to:

  ~/.kaggle/kaggle.json
  chmod 600 ~/.kaggle/kaggle.json

- The dataset will be automatically downloaded when the ETL script runs.

------------------------------------------------------------------------

# ▶️ Running the Pipeline

## Step 1 --- Run ETL(Extraction + Transformation + Load)

python scripts/transform_load.py

This will:
- Automatically download dataset from Kaggle
- Create SQLite database (supermarket.db)
- Create dimension and fact tables
- Load transformed data

## Step 2 --- Run Analytical Report

python scripts/run_report.py

The report:
- Joins fact and dimension tables
- Aggregates total sales by product line
- Uses RANK() window function to rank product lines by revenue

------------------------------------------------------------------------

# ☁️ Proposed Cloud Deployment Architecture (GCP)

-   Cloud Scheduler --- Trigger pipeline
-   Cloud Function --- Extract data using Kaggle API
-   Cloud Storage --- Extract data using Kaggle API
-   Dataflow / Cloud Function --- Transform data
-   BigQuery --- Data warehouse (dim + fact tables)
-   Looker Studio --- Reporting & dashboards

------------------------------------------------------------------------

# 📁 Project Structure

supermarket-data-pipeline/
│
├── scripts/
│   ├── extract.py
│   ├── transform_load.py
│   └── run_report.py
│
├── sql/
│   ├── create_tables.sql
│   └── report.sql
│
├── data/ (auto-created, not versioned)
├── .gitignore
└── README.md

------------------------------------------------------------------------

# 👤 Author

Doss Napoleon
Data Engineer