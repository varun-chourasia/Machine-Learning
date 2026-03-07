# Project_Models

## Overview

The **Project_Models** folder serves as a repository for complete, end-to-end machine learning project implementations. This directory contains practical examples that demonstrate the full machine learning workflow from data preparation through model deployment, providing hands-on experience with real-world applications.

## Folder Structure

```
Project_Models/
└── Iris/
    ├── Iris.ipynb
    ├── iris.py
    └── iris_model.pkl
```

## Projects

### Iris Flower Classification Project

#### Overview
A comprehensive machine learning project implementing classification on the classic Iris dataset. This project demonstrates best practices for model development, evaluation, and deployment using both Jupyter notebooks and interactive web applications.

#### Files

| File | Description |
|------|-------------|
| **[Iris.ipynb](Iris/Iris.ipynb)** | Main analysis and training notebook covering data exploration, model training, evaluation, and visualization using scikit-learn pipelines |
| **[iris.py](Iris/iris.py)** | Streamlit web application for real-time iris flower species prediction with interactive sliders for flower measurements |
| **[iris_model.pkl](Iris/iris_model.pkl)** | Serialized scikit-learn pipeline containing the trained Random Forest classifier and StandardScaler for deployment |

#### Key Features

**Iris.ipynb - Model Development:**
- Data loading from scikit-learn's Iris dataset (150 samples, 4 features, 3 species)
- Train-test split (80/20) with stratified sampling
- Pipeline architecture: StandardScaler + RandomForestClassifier
- Model evaluation with accuracy metrics and classification reports
- Confusion matrix visualization using seaborn heatmaps
- Species-specific analysis (focusing on Virginica species statistics)

**iris.py - Web Deployment:**
- Interactive Streamlit application for real-time predictions
- User-friendly sliders for sepal/petal length and width inputs
- Model loading from serialized pickle file
- Clean prediction display with species classification results

#### Dataset
- **Iris Dataset:** Classic multivariate dataset introduced by Ronald Fisher in 1936
- **Features:** Sepal length/width, petal length/width (all in cm)
- **Target Classes:** Setosa, Versicolor, Virginica (3 species)
- **Samples:** 50 samples per species, total 150 samples

#### Technical Stack
- **Machine Learning:** scikit-learn (RandomForestClassifier, Pipeline, StandardScaler)
- **Data Handling:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Web Deployment:** Streamlit
- **Model Serialization:** joblib

#### Learning Outcomes

After completing this project, you will understand:

1. Complete ML workflow from data to deployment
2. Pipeline implementation for reproducible preprocessing
3. Model evaluation and performance metrics
4. Web application development for model serving
5. Model serialization and loading for production use

## Project Workflow

1. **Data Preparation:** Load and explore the Iris dataset
2. **Model Training:** Build and train Random Forest classifier with scaling
3. **Model Evaluation:** Assess performance using various metrics
4. **Model Serialization:** Save trained model for deployment
5. **Web Application:** Create interactive prediction interface
6. **Deployment:** Serve model via Streamlit for real-time predictions

## Prerequisites

- Completion of foundational modules ([Machine Learning Foundation](../Machine%20Learning%20Foundation/), [ML_Preprocessing](../ML_Preprocessing/))
- Basic understanding of classification algorithms
- Familiarity with Jupyter notebooks and Python scripting

## Dependencies

See the main [requirements.txt](../requirements.txt) for required packages. Additional project-specific packages:
- streamlit (for web application)
- joblib (for model serialization)

## Running the Project

### Training and Analysis
```bash
jupyter notebook Project_Models/Iris/Iris.ipynb
```

### Web Application
```bash
streamlit run Project_Models/Iris/iris.py
```

## Future Projects

This folder is designed to expand with additional end-to-end projects such as:
- House price prediction using regression
- Customer churn classification
- Image classification projects
- Time series forecasting
- Natural language processing applications

## Related Folders

- **[Machine Learning Foundation](../Machine%20Learning%20Foundation/)**: Basic algorithms used in projects
- **[ML_Preprocessing](../ML_Preprocessing/)**: Preprocessing techniques applied in projects
- **[Model Deployment and Production](../Model%20Deployment%20and%20Production/)**: Advanced deployment strategies beyond Streamlit</content>
<parameter name="filePath">d:\Machine Learning\Project_Models\README.md