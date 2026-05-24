# Table of Content
---
- Data Preprocessing in Python
- Data Preprocessing Include
- Feature Scaling: Normalization and Standardization
- Advantages
---

# Data Preprocessing in Python
Data preprocessing is the first step in any data analysis or machine learning pipeline. It involves cleaning, transforming and organizing raw data to ensure it is accurate, consistent and ready for modeling. It has a big impact on model building such as:
- Clean and well-structured data allows models to learn meaningful patterns rather than noise.
- Properly processed data prevents misleading inputs, leading to more reliable predictions.
- Organized data makes it simpler to create useful inputs for the model, enhancing model performance.
- Organized data supports better Exploratory Data Analysis (EDA), making patterns and trends more interpretable.

# Data Preprocessing Include:
- Data Cleaning
- Sampling Data
- Dimensionality Reduction
- Data Transformation
- Feature Engineering
- Imbalanced Data

# Feature Scaling: Normalization and Standardization
Scale features to a common range or distribution, important for many ML algorithms sensitive to feature magnitudes.
## 1. Normalization (Min-Max Scaling)
- Rescales features between 0 and 1. Good for algorithms like k-NN and neural networks.
- Class: MinMaxScaler from sklearn.
- .fit_transform(): Learns min/max from data and applies scaling.
## 2. Standardization
- Transforms features to have mean = 0 and standard deviation = 1, useful for normally distributed features.
- Class: StandardScaler from sklearn.


# Advantages
- **Improves Data Quality:** Cleans and organizes raw data for better analysis.
- **Enhances Model Accuracy:** Removes noise and irrelevant data, leading to more precise predictions.
- **Reduces Overfitting:** Handles outliers and redundant features, improving model generalization.
- **Speeds Up Training:** Efficiently scaled data reduces computation time.
- **Ensures Algorithm Compatibility:** Converts data into formats suitable for machine learning models.