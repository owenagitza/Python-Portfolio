### Table of Contents

- [Description](#description)
- [Problem Statement](#problem-statement)
- [Dataset Information](#dataset-information)
- [Contents](#contents)
- [Additional Resources](#additional-resources)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## Description

This notebook provides an end-to-end demonstration of **Olist E-commerce analytics: Sentiment classification using machine learning**. The scope of topics discussed in this notebook includes data analysis & machine learning (supervised classification, imbalanced dataset problem, hyperparameter tuning, threshold moving, etc.)

---

## Problem Statement

Reviews are an integral part of any e-commerce business. They capture direct feedback from customers about products and most importantly, they are mostly freely given to the company. Hence, it is important to leverage this abundant information and create important signals to send feedback to the e-commerce system so that it can use them to further improve the customer experience. Moreover, reviews can be viewed by all customers, and they directly affect the sales of the products [Vajjala et al., 2020].

The traditional way of garnering feedback for companies has been through surveys, closed user group testing, and so on. These methods have a considerable drawback including:
- Manual methods of review analysis can be resource extensive in terms of time and money
- Review analysis even more challenging by nature. They’re in the text and mostly in an unstructured format, full of unforced errors such as spelling mistakes, incorrect sentence constructions, incomplete words, and abbreviations

As the frontline of e-commerce business in Brazil, Olist may find the automation of review analysis useful since Olist has a large database of user reviews at its disposal. One such utilization of reviews is **sentiment analysis**. Sentiment analysis has been one of the most active research areas in natural language processing since early 2000 . The aim of sentiment analysis is to define automatic tools able to extract subjective information from texts in natural language, such as opinions and sentiments, so as to create structured and actionable knowledge to be used by either a decision support system or a decision maker [Pozzi et al., 2016].

Hence, this notebook tries to perform a sentiment analysis model that could sort through thousands of reviews and grasp the overall sentiment of customers in an instance. Furthermore, by the end of this notebook, I wish to answer the following questions:
1. What is the best modeling approach to be used for this sentiment analysis?
    - What model performs the best?
    - How does the best model's performance compare to the other models?
1. How is the overall sentiment of customer reviews? What terms are found in both good and bad reviews?
1. What recommended actions should be taken considering this information? How does it translate to actionable business decisions?

---

## Dataset Information

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

This dataset is a real commercial data of orders made at Olist. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. For completeness, it also includes a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where he can give a note for the purchase experience and write down some reviews.

**Attention**
1. An order might have multiple items.
1. Each item might be fulfilled by a distinct seller.
1. All text identifying stores and partners where replaced by the names of Game of Thrones great houses.

---

## Contents

    0. Preface
      0.1. Library
      0.2. User-defined Functions

    1. Business Understanding
      1.1. Context
      1.2. Problem Statement
      1.3. Objectives
      1.4. Analytic Approach
      1.5. Evaluation Metric
      1.6. References

    2. Data
      2.1. Dataset Information
      2.2. Dataset Preview
        2.2.1. Geolocation Dataset
        2.2.2. Customers Dataset
        2.2.3. Order Items Dataset
        2.2.4. Payments Dataset
        2.2.5. Reviews Dataset
        2.2.6. Orders Dataset
        2.2.7. Products Dataset
        2.2.8. Sellers Dataset
      2.3. Dataset Processing
        2.3.1. Reviews Dataset (Main)
      2.4. Combining Datasets
        2.4.1. Table 1. Orders-reviews-order Items
        2.4.2. Table 2. Orders-reviews-customers-order Items-sellers

    3. Exploratory Data Analysis
      3.1. Data Frame Processing
        3.1.1. How's The Order Density Across States? How's Their Sentiment Proportions?
        3.1.2. How's The Order Density Across States? How's Their Sentiment Proportions?
        3.1.3. How's The Difference Of Delivery Path Between Orders With Positive And Negative Sentiments?
        3.1.4. How's The Distribution Of Delivery Dates Between Orders With Positive And Negative Sentiments? Is It Statistically Different?
        3.1.5. How's Seller State's Performance In Terms Of Delivery Day Difference?
     3.2. Data Visualization And Statistics
        3.2.1. How's The Order Density Across States? How's Their Sentiment Proportions?
        3.2.2. How's The Order Density Across States? How's Their Sentiment Proportions?
        3.2.3. How's The Difference Of Delivery Path Between Orders With Positive And Negative Sentiments?
        3.2.4. How's The Distribution Of Delivery Dates Between Orders With Positive And Negative Sentiments? Is It Statistically Different?
        3.2.5. How's Seller State's Performance In Terms Of Delivery Day Difference?
      3.3. Tableau Dashboard

    4. Machine Learning
      4.1. Data Preparation
      4.2. Text Preprocessing
      4.3. Sentiment Content & Length Of Sentence
      4.4. Base Model Evaluation
      4.5. Base Model Evaluation With Oversampling (Smote)
      4.6. Base Model Evaluation With Undersampling (Nearmiss)
      4.7. Base Model Output Recap
      4.8. Hyperparameter Tuning - Logistic Regression
      4.9. Feature Importance
      4.10. Implementation
      4.11. Learning Curve

    5. Conclusion & Recommendation

---

## Additional Resources
Due to the file limit of GitHub, additional resources are posted on [Google Drive](https://drive.google.com/drive/folders/1UER2T0Fhsn9cJopTSkaQGXBLn_wPIQhR?usp=share_link). You can find the folders:
1. Dataset
1. Resources

to be downloaded and combine it with the files downloaded from this repository into the respective directory.

---

## How To Use

To get the notebook, simply download or clone this repository.  From there, you can open it up in a text editor.

**Please make sure to download the zip file and extract all of the contents. DO NOT change the structure of the folders to ensure that the notebook is viewed as intended.**

---

## Author Info

- LinkedIn - [Owen Agitza](https://www.linkedin.com/in/owenagitza/)