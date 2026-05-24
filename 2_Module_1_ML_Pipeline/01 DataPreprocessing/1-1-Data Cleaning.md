# Table of Content
---
- Data Cleaning
- Benefit of Data Cleaning
- How to Perform Data Cleaning
- Data formatting
- Data Cleaning Tools
- Advantages
- Disadvantages
---

# Data Cleaning
Data cleaning involves identifying and removing any **missing**, **duplicate** or **irrelevant** data.

- Raw data (log file, transactions, audio /video recordings, etc) is often **noisy**, **incomplete** and **inconsistent** which can negatively impact the accuracy of the model.
- The goal of data cleaning is to ensure that the data is **accurate**, **consistent** and **free of errors**.
- Clean datasets are also **important in EDA (Exploratory Data Analysis)**, which enhances the interpretability of data so that the right actions can be taken based on insights.

# Benefit of Data Cleaning
- Error Free Data
- Data Quality
- Accuracy & Efficiency
- Complete Data
- Maintains Data Consistency

# How to Perform Data Cleaning
- **Remove Unwanted Observations:** Eliminate **duplicates**, **irrelevant** entries or **redundant** data that add noise.
  - EX: Remove duplicate customer records that appear multiple times in the dataset.
- **Fix Structural Errors:** Standardize data formats and variable types for consistency.
  - EX: Convert all date formats to a unified format like “2023‑05‑10” for consistency.
- **Manage Outliers:** Detect and handle extreme values that can skew results, either by removal or transformation.
  - EX: Detect unusually high transaction amounts and cap them to reduce skewness.
- **Handle Missing Data:** Address gaps using imputation, deletion or advanced techniques to maintain accuracy and integrity.
  - EX: Fill missing age values using the mean or median to preserve data completeness.

# Data formatting
Data formatting involves converting the data into a standard format or structure that can be easily processed by the algorithms or models used for analysis. Here we will discuss commonly used data formatting techniques i.e. Scaling and Normalization.
## 1. Min-Max Scaling
Scaling involves transforming the values of features to a specific range. Min-Max scaling rescales the values to a specified range, typically between 0 and 1. It preserves the original distribution and ensures that the minimum value maps to 0 and the maximum value maps to 1.
## 2. Standardization (Z-score scaling)
Standardization transforms the values to have a mean of 0 and a standard deviation of 1. It centers the data around the mean and scales it based on the standard deviation. Standardization makes the data more suitable for algorithms that assume a Gaussian distribution or require features to have zero mean and unit variance.
- Formula: Z = (X - μ) / σ
  - X = Data
  - μ = Mean value of X
  - σ = Standard deviation of X

# Data Cleaning Tools
- **OpenRefine:** A free, open-source tool for cleaning, transforming and enriching messy data with an easy-to-use interface and powerful features like clustering and faceting.
- **Trifacta Wrangler:** An AI-powered, user-friendly platform that helps automate data cleaning and transformation workflows for faster, more accurate preparation.
- **TIBCO Clarity:** A data profiling and cleansing tool that ensures high-quality, standardized and consistent datasets across diverse sources.
- **Cloudingo:** A cloud-based solution focused on deduplication and data cleansing, especially useful for maintaining accurate CRM data.
- **IBM InfoSphere QualityStage:** An enterprise-grade tool designed for large-scale, complex data quality management including profiling, matching and cleansing.

# Advantages 
- Removing errors, inconsistencies, and irrelevant data helps the model learn better from the data.
- Ensures the data is accurate, consistent, and free of errors.
- Transforms data into a format that better represents underlying patterns and relationships.
- Improves data quality, making it more reliable and accurate.
- Helps identify and remove sensitive or confidential information, improving data security.

# Disadvantages
- It is time-consuming, especially for large and complex datasets.
- It can lead to loss of important information if not handled carefully.
- Requires significant time, effort, expertise, and sometimes specialized tools.
- Removing too much data can contribute to overfitting.


