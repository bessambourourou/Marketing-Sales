USE PortfolioProject_MarketingAnalytics;
*-*******************************************
*********************************************
/*customer_reviews*/
select 
r.ReviewID,
c.CustomerName,
p.ProductName, 
r.ReviewDate as date_of_Review ,
r.Rating as rating,
r.ReviewText as the_Review
from  dbo.customer_reviews r 
left join dbo.customers as c on c.CustomerID=r.CustomerID
left join dbo.products as p on r.ProductID = p.ProductID
