select  C.country,  Cat.categoryname 
from Customers C
Join Orders O On C.customerid = O.customerid
Join "Order Details" OD on OD.orderid = O.orderid
Join Products P On P.productid = OD.productid
Join Categories Cat on Cat.CategoryID = P.categoryid
