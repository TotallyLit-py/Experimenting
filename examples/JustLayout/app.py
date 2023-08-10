import streamlit as st

import totallylit as lit

lit.init()

st.header("hi!")


@lit.page("Home")
def home():
    st.header("Hi from Home")


@lit.page
def name_not_given():
    st.header("Hi from name_not_given")


for page in lit.context.app.pages:
    st.write(f"{page.name} - {page.title}")

st.write(f"ROOT: {lit.context.app.info.root_folder}")
