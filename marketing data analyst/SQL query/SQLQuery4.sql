USE PortfolioProject_MarketingAnalytics;

SELECT 'customers' AS tbl, COUNT(*) AS row_count FROM dbo.customers
UNION ALL SELECT 'geography', COUNT(*) FROM dbo.geography
UNION ALL SELECT 'products', COUNT(*) FROM dbo.products
UNION ALL SELECT 'customer_journey', COUNT(*) FROM dbo.customer_journey
UNION ALL SELECT 'customer_reviews', COUNT(*) FROM dbo.customer_reviews
UNION ALL SELECT 'engagement_data', COUNT(*) FROM dbo.engagement_data;
   ²
