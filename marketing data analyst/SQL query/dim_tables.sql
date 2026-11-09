USE PortfolioProject_MarketingAnalytics;
************************************************************
***********************************************************
/*products table -*/
select * from dbo.products


select 
	ProductID,
	ProductName ,
	Price, 
    CASE when Price <50 then 'low'
	     when Price between 50 and 200 then 'medium'
		 else 'high'
    end category
from dbo.products 
order by category 


**************************************************************
************************************************************
/*customer and geography tables */


select  * from  dbo.customers 
select * from dbo.geography



select 
c.CustomerID ,
c.CustomerName, 
c.Email,
c.Gender,
c.Age,
g.Country,
g.City
from dbo.customers as c
left join dbo.geography g
on  c.GeographyID = g.GeographyID
