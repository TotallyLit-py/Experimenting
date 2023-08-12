import streamlit as st

import totallylit as lit

lit.init()

st.markdown(
    """
<style>
[data-testid="tooltipHoverTarget"] {
    display: none;
    color: blue;
}
</style>
""",
    unsafe_allow_html=True,
)

# [data-testid=stSidebar] {
#     background-color: #fff;
#     color: #000;
# }


@lit.page("Home")
def home():
    st.header("Hi from Home")


@lit.page
def name_not_given():
    st.header("Hi from name_not_given")


st.write(f"ROOT: {lit.context.app.info.root_folder}")

if "current_page_name" not in st.session_state:
    st.session_state["current_page_name"] = "home"

lit.context.app.get_page(st.session_state["current_page_name"]).function()


def on_page_link_click(page_name: str):
    st.session_state["current_page_name"] = page_name


st.write("<a href='#' id='my-link'>Click me</a>", unsafe_allow_html=True)

if st.button("my-link"):
    st.write("Link clicked!")

with st.sidebar:
    for page in lit.context.app.pages:
        st.write(page.name)
        st.button(
            f"{page.name} - {page.title}",
            on_click=on_page_link_click,
            args=(page.name,),
            type="primary",
            help="this is the help",
            key=f"this-is-the-key:{page.name}",
        )
        st.button(
            f"NO KEY {page.name} - {page.title}",
            on_click=on_page_link_click,
            args=(page.name,),
            type="primary",
        )
