import streamlit as st
import pandas


def render_profile(row_arg):
    st.subheader(f"{row_arg['first name']} {row_arg['last name']}".title())
    st.write(row_arg["role"])
    st.image("images/" + row_arg["image"])


lipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
 ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
 laboris nisi ut aliquip ex ea commodo consequat.
"""
df = pandas.read_csv("data.csv")
st.set_page_config(layout="wide")

st.header("The Best Company")
st.write(lipsum)
st.subheader("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

with col1:
    for index, row in df[:4].iterrows():
        render_profile(row)

with col2:
    for index, row in df[4:8].iterrows():
        render_profile(row)

with col3:
    for index, row in df[8:].iterrows():
        render_profile(row)