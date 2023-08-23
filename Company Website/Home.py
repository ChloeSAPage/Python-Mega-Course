import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
         sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
         ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
         reprehenderit in voluptate velit esse cillum dolore eu fugiat 
         nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
         sunt in culpa qui officia deserunt mollit anim id est laborum
         """)

st.subheader("Our team")

col1, blank, col2, blank2, col3 = st.columns([1.5,0.5,1.5,0.5,1.5])

data = pandas.read_csv("data.csv")

with col1:
    for index, row in data[:4].iterrows():
        names = (f"{row['first name'].capitalize()}"
        f" {row['last name'].capitalize()}")
        st.header(names)
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in data[4:8].iterrows():
        names = (f"{row['first name'].capitalize()}"
        f" {row['last name'].capitalize()}")
        st.header(names)
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in data[8:].iterrows():
        names = (f"{row['first name'].capitalize()}"
        f" {row['last name'].capitalize()}")
        st.header(names)
        st.write(row["role"])
        st.image(f"images/{row['image']}")