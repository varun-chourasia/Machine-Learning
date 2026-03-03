import streamlit as st
import joblib
import numpy as np

model = joblib.load('iris_model.pkl')

st.title("Iris Flower Predictor")
st.write("Enter the measurements to predict the flower type:")

s_length = st.slider("sepal length",4.0,8.0)
s_width = st.slider("sepal width",2.0,5.0)
p_length = st.slider("Petal length",1.0,7.0)
p_width = st.slider("Petal width",0.1,2.5)

if st.button("Predict"):
    features = np.array([[s_length,s_width,p_length,p_width]])
    prediction = model.predict(features)


    target_names = ['Setosa', 'Versicolor', "Virginica"]
    result = target_names[prediction[0]]

    st.success(f" The Flower is: **{result}**")