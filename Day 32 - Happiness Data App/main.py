import streamlit as st
import plotly.express as px

st.title("In Search for Happiness")

dataX = st.selectbox("Select data for X-Axis",
                        ("GDP", "Happiness", "Generosity"))
dataY = st.selectbox("Select data for Y-Axis",
                        ("GDP", "Happiness", "Generosity"))
st.subheader(f"{dataX} and {dataY}")

GDP = [570, 578, 636]
Happiness = [5003, 5048, 5122]
Generosity = [165, 185, 178]

figure = px.scatter(x=dataX, y=dataY, labels={"x": "xaxis", "y": "yaxis"})

st.plotly_chart(figure)