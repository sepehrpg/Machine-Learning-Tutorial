# Table of Content
--- 
- Feature Engineering - Scaling, Normalization and Standardization
- Feature Engineering Include
- It contributes to model building in the following ways
- Scaling Types
- Comparison of Various Feature Scaling Techniques
- Advantages
---


# Feature Engineering - Scaling, Normalization and Standardization
Well-designed Feature engineering is the process of **creating**, **transforming** or **selecting important features** from raw data to improve model performance. These features help the model capture useful patterns and relationships in the data.

# Feature Engineering Include
- Scaling
- Normalization
- Standardization

# It contributes to model building in the following ways:
- Well-designed features help the model to learn complex patterns more effectively.
- Removing noise and irrelevant information improves model prediction accuracy.
- Focusing on meaningful features helps the model to generalize better and reduces overfitting.
- Clear and informative features make the model easier to understand and interpret.

# Scaling Types

## 1. Absolute Maximum Scaling
Absolute Maximum Scaling is a feature scaling method where each value is divided by the maximum absolute value of that feature. 
- This transformation rescales the data so that values fall within the range of −1 to 1.
- Sensitive to Outliers: Extreme values can affect the maximum value and reduce scaling quality.
- Best for Clean Data: Works better when the dataset does not contain strong outliers.
- **What it does:** Scales data to \([-1, 1]\) based on the maximum absolute value.
- **When to use:** When data is already centered around 0 and is sparse (many zeros).
- **Pros:** Preserves sparsity (zeros stay zero); computationally light.
- **Cons:** Still sensitive to very large values; uses a single scale factor for the whole feature. 
### Scaling Formula:
$$
X_{\rm {scaled }}=\frac{X_{i}}{\rm{max}\left(|X|\right)} 
$$

## 2. Min-Max Scaling
Min-Max Scaling rescales features by subtracting the minimum value and dividing by the difference between the maximum and minimum values. 
- This usually maps feature values to the range 0 to 1 while preserving the original distribution.
- **What it does:** Maps features to a fixed range, typically \([0, 1]\). 
- **When to use:** When you need bounded features (e.g., for neural nets, distance-based models like k-NN, SVM).
- **Pros:** Simple, intuitive, preserves shape of distribution, keeps relative distances. 
- **Cons:** Very sensitive to outliers; min and max can be heavily distorted by a few extreme values. 
### Scaling Formula:
$$
X_{\rm {scaled }}=\frac{X_{i}-X_{\text {min}}}{X_{\rm{max}} - X_{\rm{min}}} 
$$


## 3. Standardization
Standardization scales features by subtracting the mean and dividing by the standard deviation. This transforms the data so that features have zero mean and unit variance, which helps many machine learning models perform better.
- **What it does:** Produces features with mean 0 and variance 1.
- **When to use:** For most linear models, SVM, Logistic Regression, PCA, and many gradient-based methods.
- **Pros:** Classic standardization; works well when data is approximately Gaussian; common default.
- **Cons:** Sensitive to outliers; \(\mu\) and \(\sigma\) can be heavily influenced by extreme values.
### Scaling Formula:
$$
X_{\rm {scaled }}=\frac{X_{i}-\mu}{\sigma} 
$$
Where:
- \( \mu \) = mean
- \( \sigma \) = standard deviation
- Produces features with mean 0 and variance 1
- Effective for data that is approximately normally distributed


## 4. Robust Scaling
Robust Scaling scales features using the median and interquartile range (IQR) instead of the mean and standard deviation. This makes it less sensitive to outliers and skewed data, making it suitable for datasets with extreme values or noise.
- **What it does:** Centers data by the median and scales by IQR (Q3 − Q1).
- **When to use:** When data contains many outliers or is strongly skewed.
- **Pros:** Very robust to outliers; uses median and IQR instead of mean and standard deviation.
- **Cons:** If the distribution is already clean and close to normal, it may slightly distort fine detail.
### Scaling Formula:
$$
X_{\rm {scaled }}=\frac{X_{i}-X_{\text {median }}}{IQR} 
$$
Where:
- \( X_i \) is each individual value.
- \( X_{\text{median}} \) is the median of \( X \).
- \( IQR \) is the interquartile range, defined as \( IQR = Q_3 - Q_1 \).
- Centers the data around the median and scales it by the spread of the middle 50% of values.
- Robust to outliers compared to mean/standard-deviation scaling.


## 5. Normalization (Vector Normalization)
Normalization scales each data sample so that its vector length (Euclidean norm) becomes 1. It focuses on the direction of data points rather than their magnitude, making it useful in tasks like text classification and clustering.
### Scaling Formula:
$$
X_{\text{scaled}} = \frac{X_i}{\| X \|} 
$$
Where:
- \( X_i \) is each individual value.
- \( \lVert X \rVert \) represents the Euclidean norm (or length) of the vector \( X \).
- This normalization scales each sample to unit length.
- Useful for direction-based similarity metrics.
- So:
\[
\|X\|_2 = \sqrt{x_1^2 + x_2^2 + \dots + x_d^2}
\]


## 6. L1 Normalization (Manhattan / Taxicab Normalization)

L1 Normalization rescales each **sample (row)** so that the sum of the absolute values of its components equals 1. It focuses on the **relative contribution** of each feature within the same sample.

### Scaling Formula:
$$
X_{\text{scaled}} = \frac{X_i}{\sum_j \lvert X_j \rvert}
$$

Where:
- \( X_i \) is each individual value in a sample vector \( X \).
- \( \sum_j \lvert X_j \rvert \) is the L1 norm (sum of absolute values) of that sample.
- Each sample is transformed so that its L1 norm becomes 1.

Key points:
- Operates **per sample**, not per feature (each row is normalized independently).
- Emphasizes the **proportions** or **relative weights** of features in a sample.
- Useful when:
  - You work with **sparse data** (e.g., text features, TF–IDF).
  - You care about the **distribution of weights** in each example more than absolute magnitude.

---

## 7. L2 Normalization (Euclidean Normalization)

L2 Normalization rescales each **sample (row)** so that the Euclidean length (L2 norm) of its vector equals 1. It focuses on the **direction** of the vector rather than its magnitude.

### Scaling Formula:
$$
X_{\text{scaled}} = \frac{X_i}{\sqrt{\sum_j X_j^2}}
$$

Where:
- \( X_i \) is each individual value in a sample vector \( X \).
- \( \sqrt{\sum_j X_j^2} \) is the L2 norm (Euclidean length) of that sample.
- Each sample is transformed so that its L2 norm becomes 1.

Key points:
- Operates **per sample**, not per feature.
- Keeps the **direction** of the vector but ignores overall length.
- Very common when:
  - You use **cosine similarity** or other **direction-based** similarity measures.
  - You work with **text embeddings**, TF–IDF vectors, or other high-dimensional representations.
  - You want to compare samples by their orientation in feature space rather than absolute scale.



# Comparison of Various Feature Scaling Techniques

| Technique         | Formula                                                                 | What it does                                                 | When to use                                                                                  | Pros                                                                                     | Cons                                                                                           |
|------------------|-------------------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Min–Max Scaling  | \( X_{\mathrm{scaled}} = \dfrac{X_i - X_{\min}}{X_{\max} - X_{\min}} \) | Maps features to a fixed range, typically \([0, 1]\).        | When you need bounded features (e.g., for neural nets, distance-based models like k-NN, SVM). | Simple, intuitive, preserves shape of distribution, keeps relative distances.            | Very sensitive to outliers; min and max can be heavily distorted by a few extreme values.      |
| Max–Abs Scaling  | \( X_{\mathrm{scaled}} = \dfrac{X_i}{\max\left( \lvert X \rvert \right)} \) | Scales data to \([-1, 1]\) based on the maximum absolute value. | When data is already centered around 0 and is sparse (many zeros).                           | Preserves sparsity (zeros stay zero); computationally light.                            | Still sensitive to very large values; uses a single scale factor for the whole feature.        |
| Standardization  | \( X_{\mathrm{scaled}} = \dfrac{X_i - \mu}{\sigma} \)                   | Produces features with mean 0 and variance 1.                | For most linear models, SVM, Logistic Regression, PCA, and many gradient-based methods.       | Classic standardization; works well when data is approximately Gaussian; common default. | Sensitive to outliers; \(\mu\) and \(\sigma\) can be heavily influenced by extreme values.     |
| Robust Scaling   | \( X_{\mathrm{scaled}} = \dfrac{X_i - X_{\text{median}}}{IQR} \)        | Centers data by the median and scales by IQR (Q3 − Q1).      | When data contains many outliers or is strongly skewed.                                       | Very robust to outliers; uses median and IQR instead of mean and standard deviation.     | If the distribution is already clean and close to normal, it may slightly distort fine detail. |
| L1 Normalization | \( X_{\mathrm{scaled}} = \dfrac{X_i}{\sum_j \lvert X_j \rvert} \)       | Normalizes each sample (row) to have L1 norm = 1.            | For models that care about relative weights within a sample (e.g., some text models, TF–IDF). | Good for sparse data (e.g., text/TF–IDF); highlights relative proportions in a sample.  | Operates per sample, not per feature; can make individual feature magnitudes harder to interpret. |
| L2 Normalization | \( X_{\mathrm{scaled}} = \dfrac{X_i}{\sqrt{\sum_j X_j^2}} \)            | Normalizes each sample (row) to have Euclidean norm = 1.     | For direction-based similarity metrics (cosine similarity, dot-product-based models).         | Emphasizes vector direction rather than absolute length; standard for text and embeddings. | Like L1, it is per-sample; better for “shape of the vector” than for preserving physical scale of features. |





# Advantages
- Improves Model Performance: Enhances accuracy and predictive power by presenting features in comparable scales.
- Speeds Up Convergence: Helps gradient-based algorithms train faster and more reliably.
- Prevents Feature Bias: Avoids dominance of large-scale features, ensuring fair contribution from all features.
- Increases Numerical Stability: Reduces risks of overflow/underflow in computations.
- Facilitates Algorithm Compatibility: Makes data suitable for distance- and gradient-based models like SVM, KNN and neural networks.