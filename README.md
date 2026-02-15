# Supermarket Data Pipeline

## Overview

This project implements a production-grade ETL (Extract, Transform,
Load) pipeline using the Kaggle Supermarket Sales dataset.

The solution: - Extracts data using the Kaggle API - Transforms it into
a dimensional star schema - Loads it into a SQLite database - Generates
an analytical SQL report using joins and window functions

The pipeline is modular, validated, and structured following
production-ready design principles.

------------------------------------------------------------------------

## Dataset

Source: Kaggle -- Supermarket Sales Dataset\
Records: 1000 transactions\
Columns: 17 attributes including Invoice ID, Branch, City, Product line,
Sales, Quantity, Rating, etc.

### Important Modeling Decision

The dataset does **not** contain a unique customer identifier.

Therefore, instead of modeling a `customer` dimension, this solution
implements a `customer_profile` dimension based on:

-   Customer type (Member / Normal)
-   Gender (Male / Female)

This preserves dimensional modeling best practices while respecting
source data limitations.

------------------------------------------------------------------------

## Data Modeling (Star Schema)

### Dimension Tables

#### 1. dim_customer_profile

-   customer_profile_id (Primary Key)
-   customer_type
-   gender

#### 2. dim_product

-   product_id (Primary Key)
-   product_line

### Fact Table

#### fact_sales

**Grain:** One row per invoice transaction

-   invoice_id
-   customer_profile_id (Foreign Key)
-   product_id (Foreign Key)
-   branch
-   city
-   date
-   payment
-   quantity
-   unit_price
-   sales
-   gross_income
-   rating

------------------------------------------------------------------------

## ETL Process

### 1. Extract

-   Kaggle API used for dataset download
-   Dynamic CSV detection
-   Structured logging enabled

### 2. Validation & Data Quality Checks

-   Schema validation
-   Null checks
-   Invoice ID uniqueness validation
-   Sales \> 0
-   Quantity \> 0
-   Rating between 0--10

### 3. Transform

-   Surrogate keys generated for dimensions
-   Column renaming for warehouse consistency
-   Fact table created at invoice-level granularity

### 4. Load

-   Explicit SQL schema creation
-   Foreign key constraints enforced
-   Indexes created for performance optimization
-   Idempotent table creation (DROP IF EXISTS)

------------------------------------------------------------------------

## Analytical Report

Business Question:

> What is the total revenue per product line within each branch, and how
> does each product rank within its branch by revenue?

Key Features: - Joins to dimension tables - Aggregations (SUM, AVG) -
Window function using RANK() OVER (PARTITION BY)

To execute:

``` bash
sqlite3 supermarket.db
.read sql/report.sql
```

------------------------------------------------------------------------

## Project Structure

    supermarket-data-pipeline/
    │
    ├── config/
    ├── data/
    ├── logs/
    ├── sql/
    │   ├── create_tables.sql
    │   ├── indexes.sql
    │   └── report.sql
    ├── src/
    │   ├── extract.py
    │   ├── validation.py
    │   ├── transform.py
    │   ├── database.py
    │   ├── load.py
    │   ├── logger.py
    │   └── main.py
    ├── tests/
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## How to Run

### 1. Activate Virtual Environment

``` bash
source venv/bin/activate
```

### 2. Run the Pipeline

``` bash
python -m src.main
```

### 3. Execute the Analytical Report

``` bash
sqlite3 supermarket.db
.read sql/report.sql
```

------------------------------------------------------------------------

## Production Considerations

-   Modular architecture (separation of concerns)
-   Rotating logging handlers
-   Data quality enforcement before transformation
-   Explicit schema with foreign key constraints
-   Indexing for performance optimization
-   Idempotent pipeline execution

------------------------------------------------------------------------

## Future Enhancements

-   Replace SQLite with cloud data warehouse (BigQuery / Redshift)
-   Containerization using Docker
-   Airflow orchestration
-   Incremental loading strategy
-   SCD Type 2 implementation for dimensions

------------------------------------------------------------------------

## Conclusion

This solution demonstrates production-grade ETL design, dimensional
modeling best practices, SQL analytics with window functions, and
structured data quality enforcement aligned with enterprise data
engineering standards.