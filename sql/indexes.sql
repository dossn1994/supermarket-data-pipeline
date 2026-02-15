CREATE INDEX idx_fact_customer_profile
ON fact_sales(customer_profile_id);

CREATE INDEX idx_fact_product
ON fact_sales(product_id);

CREATE INDEX idx_fact_branch
ON fact_sales(branch);