### Table of Contents

- [Description](#description)
- [Database Information](#database-information)
- [How To Use](#how-to-use)
- [Problem Statement](#problem-statement)
- [Author Info](#author-info)

---

## Description

`northwind` database is a sample database that is provided by Microsoft to demonstrate the features of some of its products. The `northwind` database contains sales data for a fictitious company called *Northwind Traders*, which imports and exports specialty foods from around the world.

In this notebook, a specific version of `northwind` is used as a reference database for me to complete the data analysis project. The database is provided in the `Data` subfolder as SQL script.

---

## Database Information

Source: https://github.com/owenagitza/Python-Portfolio/blob/main/Northwind_Exploratory_Data_Analysis/Data/Northwind%20Database.sql

`northwind` database consists of 13 tables: <br>
- `categories`  : Stores information about product categories
- `customercustomerdemo`    : Serves as a connector table between `customers` and `customerdemographics`
- `customerdemographics`    : Stores information about customer descriptions
- `customers`   : Stores information about customers data
- `employees`   : Stores information about employees data
- `employeeterritories` : Serves as a connector table between `employees` and `territories`
- `orderdetails`    : Stores information about order details e.g. order quantity and discounts
- `orders`  : Stores information about order data
- `products`    : Stores information about products details
- `region`  : Stores information about region division for every territories
- `shippers`    : Stores information about product shippers i.e. expedition companies
- `suppliers`   : Stores information about product suppliers
- `territories` : Stores information about territorial responsibility of each employees

Each table listed in the database can be connected, either directly or indirectly, such that any information from this database would be interrelated.

---

## How To Use

To get the notebook, simply download or clone this repository.  From there, you can open it up in a text editor.

**Please make sure to download the zip file and extract all of the contents. DO NOT change the structure of the folders to ensure that the notebook is viewed as intended.**

---

## Problem Statement

By the end of this notebook, I wish to answer 4 questions, all of which are focusing on deriving data-driven decisions to improve **sales performance** of Northwind. In the attempt to answer these questions, I determined **products** as the main tool to achieve the objectives. <br> <br>
The questions are listed as the following:
> 1. How was the sales performance trend of the Northwind company? Was it growing or was it declining?
> 1. What products contributed the most to the Northwind's revenue on average? Who supplied them?
> 1. Was there any difference in reorder level between top 25% most sold products and bottom 25% least sold products?
> 1. Who were Northwind's most valuable customers? Was there enough evidence to justify giving them special treatments?

---

## Author Info

- LinkedIn - [Owen Agitza](https://www.linkedin.com/in/owenagitza/)