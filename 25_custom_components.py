import streamlit as st
import streamlit.components.v1 as components

st.title('Custom Components with Streamlit')

# Define a simple HTML form as a custom component
def simple_form():
    html_form = """
        <form action="#" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <input type="submit" value="Submit">
        </form>
    """
    return components.html(html_form, height=150)

simple_form()
