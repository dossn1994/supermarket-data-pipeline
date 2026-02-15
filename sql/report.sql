SELECT 
    dp.product_line,
    fs.branch,
    SUM(fs.sales) AS total_revenue,
    ROUND(AVG(fs.rating), 2) AS avg_rating,
    RANK() OVER (
        PARTITION BY fs.branch
        ORDER BY SUM(fs.sales) DESC
    ) AS revenue_rank_within_branch
FROM fact_sales fs
JOIN dim_product dp
    ON fs.product_id = dp.product_id
JOIN dim_customer_profile dcp
    ON fs.customer_profile_id = dcp.customer_profile_id
GROUP BY dp.product_line, fs.branch
ORDER BY fs.branch, revenue_rank_within_branch;