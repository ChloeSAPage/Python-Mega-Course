import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

optionX = st.selectbox("Select data for X-Axis",
                        ("GDP", "Happiness", "Generosity"))
optionY = st.selectbox("Select data for Y-Axis",
                        ("GDP", "Happiness", "Generosity"))
st.subheader(f"{optionX} and {optionY}")

df = pd.read_csv("happy.csv")

x_array = None
match optionX:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

y_array = None
match optionY:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{optionX} and {optionY}")

figure1 = px.scatter(x=x_array, y=y_array, labels={"x": optionX, "y": optionY})
st.plotly_chart(figure1)