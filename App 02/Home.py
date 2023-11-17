import streamlit as st
import pandas

st.set_page_config(page_title="Hi, I'm Chloe!", layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images\graduation photo - Copy.jpg", width=500)

with column2:
    st.title("Chloe Page")
    with open ("About_me.txt") as content:
        content = str(content.read())
        st.info(content)
        st.subheader("Below are some of my projects! Feel free to view the source code.")

col3, empty_col, col4 =st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
           

