-- Analytical Report: Total Sales by Product Line

SELECT
    dp.product_line,
    SUM(fs.sales) AS total_sales,
    RANK() OVER (ORDER BY SUM(fs.sales) DESC) AS sales_rank
FROM fact_sales fs
JOIN dim_product dp
    ON fs.product_id = dp.product_id
GROUP BY dp.product_line
ORDER BY total_sales DESC;