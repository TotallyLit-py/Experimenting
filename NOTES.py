import streamlit as st
from streamlit_javascript import st_javascript

import totallylit as lit

lit.init()

st.header("hi!")

if not "Something" in lit.random_dict:
    from datetime import datetime

    lit.random_dict["Something"] = f"LIT This is something! Created at {datetime.now()}"

if not "Something" in st.session_state:
    from datetime import datetime

    st.session_state[
        "Something"
    ] = f"STREAM This is something! Created at {datetime.now()}"

st.subheader(f"STREAM omething: {st.session_state['Something']}")
st.subheader(f"LIT omething: {lit.random_dict['Something']}")


@lit.page("Home")
def home():
    st.header("Hi from Home")


@lit.page
def name_not_given():
    st.header("Hi from name_not_given")


for page in lit.context.app.pages:
    st.write(f"{page.name} - {page.title}")

st.write(f"ROOT: {lit.context.app.info.root_folder}")

js_code = """
await new Promise(function(resolve, reject) {
    var sessionId = localStorage.getItem('session_id');
    if (sessionId === null) {
        sessionId = 'YOUR-GENERATED-UUID';
        localStorage.setItem('session_id', sessionId);
    }
    resolve(sessionId);
}).then(function(sessionId) {
    return sessionId;
});
"""

return_value = st_javascript(js_code.strip(), "CoolComponent")

if return_value:
    session_id = return_value
    st.write(f"Session ID: {session_id}")
else:
    st.write("Session ID not found!")
