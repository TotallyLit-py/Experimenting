import streamlit as st

import totallylit as lit

lit.init()


@lit.page("Home")
def home():
    st.header("Hi from Home")
    # TODO: register a memory service then uncomment the following
    # lit.memory["the_page"] = "home"


@lit.page
def name_not_given():
    st.header("Hi from name_not_given")


st.write(f"ROOT: {lit.context.app.info.root_folder}")

if "current_page_name" not in st.session_state:
    st.session_state["current_page_name"] = "home"

lit.context.app.get_page(st.session_state["current_page_name"]).function()


def on_page_link_click(page_name: str):
    st.session_state["current_page_name"] = page_name


with st.sidebar:
    for page in lit.context.app.pages:
        st.button(
            f"{page.name} - {page.title}",
            on_click=on_page_link_click,
            args=(page.name,),
            type="primary",
            help="this is the help",
        )
