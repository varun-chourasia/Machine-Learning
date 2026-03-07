# ML_Preprocessing

## Overview

The **ML_Preprocessing** folder contains comprehensive educational materials and practical examples demonstrating essential machine learning preprocessing techniques. This directory covers data encoding, feature scaling, and machine learning pipeline construction using real-world datasets, serving as a critical foundation for preparing raw data for effective model training.

## Folder Structure

```
ML_Preprocessing/
├── Encoding_techniques/
├── Feature Transformation/
├── Feature_scaling/
└── Machine_Learning_Pipelines/
```

## Subfolder Details

### 1. Encoding_techniques/

**Purpose:** Educational resources for categorical data encoding methods essential for preprocessing diverse data types.

#### Files:
- **[Encoding_foundation.ipynb](Encoding_techniques/Encoding_foundation.ipynb)**: Theoretical foundation covering 5 major encoding types (One-Hot, Label, Ordinal, Target, Binary Encoding) with explanations of when to use each method
- **[encoding_techniques.ipynb](Encoding_techniques/encoding_techniques.ipynb)**: Practical implementation on Telco Customer Churn dataset demonstrating encoding techniques and train-test split best practices
- **[Telco-Customer-Churn.csv](Encoding_techniques/Telco-Customer-Churn.csv)**: Real-world telecommunications customer dataset (7,043 records) with mixed categorical and numerical features

### 2. Feature Transformation/

**Status:** Empty folder reserved for future feature transformation techniques including polynomial features, interaction terms, and non-linear transformations.

### 3. Feature_scaling/

**Purpose:** Demonstrates the critical importance of feature scaling and its impact on model performance, particularly for distance-based and gradient optimization algorithms.

#### Files:
- **[Intro_Feature_Scaling.ipynb](Feature_scaling/Intro_Feature_Scaling.ipynb)**: Introductory concepts for feature scaling (currently empty, ready for content)
- **[knn_logistic_comparison.ipynb](Feature_scaling/knn_logistic_comparison.ipynb)**: Comparative analysis showing performance improvements with StandardScaler and MinMaxScaler on the Wine dataset

### 4. Machine_Learning_Pipelines/

**Purpose:** Comprehensive examples of ML pipelines for efficient, reproducible preprocessing and prediction workflows.

#### Files:
- **[Column_transformer.ipynb](Machine_Learning_Pipelines/Column_transformer.ipynb)**: Demonstrates ColumnTransformer for applying different transformations to different column types using the Telco dataset
- **[Prediction_without_pipeline.ipynb](Machine_Learning_Pipelines/Prediction_without_pipeline.ipynb)**: Shows traditional manual preprocessing approach on Titanic dataset, highlighting common pitfalls
- **[Predicition_with_pipeline.ipynb](Machine_Learning_Pipelines/Predicition_with_pipeline.ipynb)**: Modern pipeline approach solving manual preprocessing limitations with automated workflows
- **[train.csv](Machine_Learning_Pipelines/train.csv)** & **[tested.csv](Machine_Learning_Pipelines/tested.csv)**: Titanic survival prediction datasets
- **models/**: Directory containing serialized preprocessing objects and trained models (clf.pkl, ohe_sex.pkl, ohe_embarked.pkl, pipe.pkl)

## Key Learning Areas

| Topic | Key Concepts |
|-------|--------------|
| **Encoding** | One-Hot, Label, Ordinal, Target, and Binary encoding methods for categorical variables |
| **Scaling** | StandardScaler, MinMaxScaler, and their impact on KNN and Logistic Regression |
| **Pipelines** | ColumnTransformer, Pipeline composition, automated preprocessing workflows |
| **Best Practices** | Train-test split before preprocessing, avoiding data leakage, reproducible transformations |

## Learning Progression

1. **Foundation** → Encoding_techniques: Master categorical encoding methods
2. **Optimization** → Feature_scaling: Learn scaling importance and implementation
3. **Automation** → Machine_Learning_Pipelines: Build production-ready preprocessing workflows

## Technical Stack

- **Core Libraries:** scikit-learn, pandas, numpy
- **Transformers:** StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder
- **Pipeline Tools:** ColumnTransformer, Pipeline, make_pipeline
- **Serialization:** joblib for model persistence

## Prerequisites

- Completion of [Machine Learning Foundation](../Machine%20Learning%20Foundation/)
- Basic understanding of pandas and scikit-learn
- Familiarity with data types and preprocessing concepts

## Dependencies

See the main [requirements.txt](../requirements.txt) for all required packages.

## Next Steps

After mastering preprocessing techniques, proceed to:

- [Feature Engineering](../Feature%20Engineering/) for advanced feature creation
- [Supervised Machine Learning](../Supervised%20Machine%20Learning/) for algorithm implementation
- [Project_Models](../Project_Models/) for end-to-end applications</content>
<parameter name="filePath">d:\Machine Learning\ML_Preprocessing\README.md