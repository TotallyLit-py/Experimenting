import streamlit as st

from TotallyLit import app, page

app.reset()

st.header("Hi.")


@page("Home")
def home():
    pass


@page
def name_not_given():
    pass


st.subheader("PAGES")

for p in app.pages:
    st.write(f"PAGE: {p.name} - {p.title}")
