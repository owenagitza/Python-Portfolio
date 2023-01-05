### Table of Contents

- [Description](#description)
- [Problem Statement](#problem-statement)
- [Dataset Information](#dataset-information)
- [Contents](#contents)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## Description

This notebook provides an end-to-end demonstration of **E-commerce analytics: Customer churn prediction using machine learning**. The scope of topics discussed in this notebook includes supervised classification, imbalanced dataset problem, data analyis, hyperparameter tuning, threshold moving, etc.

---

## Problem Statement

An e-commerce company is interested to find out the behavior of their customers and possibily predict future customer churn. Churn refers to the situation where a customer of a company stops using its product and leaves the company. The success of this company is highly dependent on its ability to attract new customers while holding on to the existing ones. Therefore, this analysis would help the management team to use their budget wisely to target potential churners and hence increasing the company's bottomline.

By the end of this notebook, the author wishes to answer these questions which are listed as follows:

1. What is the best modeling approach to be used for this customer churn analysis?
    - What model performs the best?
    - How does the best model's performance compare to the other models?
1. Which factors (variables) play a significant role in the likelihood of customers to churn?
1. What recommended actions should be taken considering this information? How does it translate to actionable business decisions?

---

## Dataset Information

Source: https://github.com/owenagitza/Python-Portfolio/blob/main/E-Commerce_Analytics.Customer_Churn_Prediction/Data/data_ecommerce_customer_churn.csv

The dataset contains a range of the customers attributes collected by the company since they were registered. As such, there should be no need to expend additional resource to acquire the data for the modeling. This dataset is a modified version of the one provided by [Kaggle](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction).

| Attribute | Data type| Description |
| --- | --- | --- |
| Tenure | Numerics | The number of months that a customer has subscribed for |
| WarehouseToHome | Numerics | The distance (in kilometers) from the nearest company warehouse to customer's house |
| NumberOfDeviceRegistered | Numerics | Total number of devices registered by the same customer |
| PreferredOrderCat | Nominal | Customer's preference order category |
| SatisfactionScore | Numerics | Customer's self-rated satisfaction for company's services |
| MaritalStatus | Nominal | Current marital status |
| NumberOfAddress | Numerics | Total number of customer's address |
| Complain | Binary | 0 – Has not complained, 1 – Has complained |
| DaySinceLastOrder | Numerics | Number of days since customer's last order |
| CashbackAmount | Numerics | The total amount ($) of cashback received by the customer |
| Churn (Target) | Binary | 0 – Do not churn, 1 – Churn |

Each table listed in the database can be connected, either directly or indirectly, such that any information from this database would be interrelated.

---

## Contents

    1  BUSINESS UNDERSTANDING  
    1.1  Context  
    1.2  Problem statement  
    1.3  Objectives  
    1.4  Analytic approach  
    1.5  Evaluation metric  
    1.6  References  
    
    2  DATA  
    2.1  Dataset information
    2.2  Attribute information
    2.3  Dataset preview
        2.3.1  Dataset import
        2.3.2  General info
        2.3.3  Target proportion

    3  DATA CLEANING  
    3.1  Renaming columns  
    3.2  Missing values  
        3.2.1  Analysis  
        3.2.2  Handling missing values  
    3.3  Outliers  
        3.3.1  Analysis  
        3.3.2  Dropping outliers  
    3.4  Duplicated records  
    3.5  Data inconsistencies  
        3.5.1  object (Categorical)  
        3.5.2  int64 (Numerical)  
        3.5.3  float64 (Numerical)  
        3.5.4  Cleaned data preview  
    3.6  References  

    4  EXPLORATORY DATA ANALYSIS  
    4.1  Data frame processing  
        4.1.1  Finding registration year for every customer  
    4.2  Data visualization and statistics  
        4.2.1  Q1. How's the current composition of customers in terms of registration year?  
        4.2.2  Q2. How's the proportion of categorical variables between customers that churn and do not churn?  
            4.2.2.1  Variable: PreferredOrderCat  
            4.2.2.2  Post-hoc analysis  
            4.2.2.3  Variable: MaritalStatus  
            4.2.2.4  Variable: Complain  
        4.2.3  Q3. How's the correlation distribution of numerical variables between customers that churn and do not churn?  

    5  MODELING  
    5.1  Data preprocessing  
        5.1.1  Data transformation  
            5.1.1.1  Data splitting  
    5.2  Models  
    5.3  Benchmarking  
        5.3.1  Baseline model  
        5.3.2  Cross-validation  
        5.3.3  Benchmarking on test data  
    5.4  Imbalanced learning  
        5.4.1  Data transformation with imbalanced learning  
        5.4.2  Cross-validation with imbalanced learning  
        5.4.3  Benchmarking on test data with imbalanced learning  
    5.5  Hyperparameter tuning  
        5.5.1  Default hyperparameters  
        5.5.2  Model and hyperparameter space definition  
    5.6  References  

    6  EVALUATION  
    6.1  Tuning evaluation on test data set  
    6.2  PR-curve & threshold moving  
    6.3  Final evaluation  
        6.3.1  Final evaluation cross-validation  
        6.3.2  Final evaluation on test data  
    6.4  Feature importances  

    7  CONCLUSION & RECOMMENDATION  
    7.1  Conclusion  
    7.2  Recommendation  
    7.3  Pickle  
    7.4  References  

---

## How To Use

To get the notebook, simply download or clone this repository.  From there, you can open it up in a text editor. The final model can be accessed in the repository with the name `final_model.sav`.

**Please make sure to download the zip file and extract all of the contents. DO NOT change the structure of the folders to ensure that the notebook is viewed as intended.**

---

## Author Info

- LinkedIn - [Owen Agitza](https://www.linkedin.com/in/owenagitza/)

