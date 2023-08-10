import streamlit as st

import totallylit as lit

st.header("Hi.")


@lit.page("Home")
def home():
    pass


@lit.page
def name_not_given():
    pass


st.subheader("PAGES")

for p in lit.app.pages:
    st.write(f"PAGE: {p.name} - {p.title}")
