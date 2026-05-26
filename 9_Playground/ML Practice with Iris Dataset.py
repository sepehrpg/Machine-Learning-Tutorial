#%% md
# # Step 1: Problem Definition
# In this project, we aim to implement and evaluate several machine learning classification algorithms using the well-known Iris flower dataset. The primary objectives of this study are as follows:
# - **Objective:** To classify iris flowers into their three respective species (**Setosa**, **Versicolor**, and **Virginica**) based on four specific physical features: **sepal length**, **sepal width**, **petal length**, and **petal width**.
# - **Outcome:** By the end of this exercise, we will compare these models to determine which algorithm is most effective for this particular dataset, providing insights into their strengths and weaknesses in a multiclass classification context.
#%% md
# # Step 2: Data Collection
# In this phase, we import the Iris dataset from the scikit-learn library. This dataset is a classic benchmark in machine learning, containing 150 samples of iris flowers.
# 
# **Data Details:**
# - **Source:** sklearn.datasets.load_iris
# - **Features:** Four numerical measurements (sepal length, sepal width, petal length, and petal width in cm).
# - **Target:** Three classes representing species of the iris flower.
#%%
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Feature matrix
y = iris.target  # Target vector

# Reporting Statistics
print("--- Dataset Statistics ---")
print(f"Total number of samples: {X.shape[0]}")
print(f"Total number of features: {X.shape[1]}")
print(f"Number of classes: {len(np.unique(y))}")
print(f"Class labels: {iris.target_names}")
#%%
# Preview the data structure

df = pd.DataFrame(data=X, columns=iris.feature_names)
df['species'] = y

df.info()
df.head(n=20)
#%% md
# # Step 3: Data Cleaning and Preprocessing
# The Iris dataset is already well-structured, containing no missing values or extreme outliers. However, to ensure a robust evaluation, we must:
# - **Split the Data:** Divide the dataset into Training and Testing sets. This is a vital step to avoid overfitting and to assess how well our models perform on unseen, new data.
# - **Strategy:** We will use a 80/20 split (80% for training, 20% for testing), which is standard practice to maintain enough data for both learning and validation.
#%%
from sklearn.model_selection import train_test_split

# Splitting the data
# We set random_state=42 to ensure our results are reproducible
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Data splitting complete.")
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")
#%% md
# # Step 4: Exploratory Data Analysis (EDA)
# EDA allows us to identify patterns, correlations, and potential challenges in the dataset before training our models. For the Iris dataset, we will focus on:
# 1. Statistical Distribution: Understanding the range and distribution of each feature.
# 2. Correlation Matrix: Identifying how strongly features are related to each other.
# 3. Visual Patterns: Using pair-plots to visualize how well the classes are separated in 2D space.
# 
# Why this is important for your report:
# - **The Heatmap:** You will notice that petal length and petal width have a very high correlation with the target. This tells you that these two features will likely be the most important for your Decision Tree and SVM models.
# - **The Pairplot:** Look at the clusters. You will see that Setosa (the blue cluster) is clearly separated from the others, while Versicolor and Virginica have some overlap.
#     - **Pro-tip for your report:** Mention that "The linear overlap between Versicolor and Virginica explains why some models might struggle slightly more to classify these two classes compared to Setosa."
# 
# ### The Insight:
# ### The Decision:
#%%
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Descriptive Statistics
print("--- Statistical Summary of Features ---")
pd.DataFrame(X, columns=iris.feature_names).describe()
#%%
# 2. Correlation Heatmap
# This shows us if features are highly correlated (which can impact some models)
plt.figure(figsize=(8, 6))
sns.heatmap(pd.DataFrame(X, columns=iris.feature_names).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()
#%%
# 3. Pairplot
# This is the most powerful visualization for Iris. It shows the distribution 
# of each feature and the relationship between every pair of features.
sns.pairplot(df, hue='species', palette='viridis', markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Features by Species", y=1.02)
plt.show()
#%% md
# # Step 5: Feature Engineering and Selection
# While the Iris dataset features are already well-defined, in a professional workflow, this stage is crucial for:
# 1. **Feature Engineering:** Creating new variables that might better represent the underlying patterns.
# 2. **Feature Selection:** Determining which features contribute most to the model's predictive power.
# 
# In this specific case, we will use a **Random Forest Classifier** as a heuristic tool to calculate "Feature Importance." This helps us understand which physical measurements (sepal/petal length and width) are the primary drivers in classifying the iris species.
# 
# ### The Insight:
# ### The Decision:
#%%
from sklearn.ensemble import RandomForestClassifier

# Using a Random Forest to calculate feature importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Getting importance scores
importances = rf.feature_importances_
feature_names = iris.feature_names

# Plotting the feature importance
plt.figure(figsize=(8, 4))
plt.barh(feature_names, importances, color='skyblue')
plt.title("Feature Importance (via Random Forest)")
plt.xlabel("Importance Score")
plt.show()

print("Feature Importance Scores:")
for name, imp in zip(feature_names, importances):
    print(f"{name}: {imp:.4f}")
#%%
