# Custom imports
import streamlit as st
from multipage import MultiPage
from sites import live_demonstration, project_overview
from PIL import Image

# Create an instance of the app
app = MultiPage()

# Title of the main page
col1, col2 = st.columns(2)

with col1:
    st.title("Master Thesis")
    st.subheader("Automated categorisation for Products in the Life-Science Sector with Natural Language Processing")
    st.write("from Simon Glauser")

with col2:
    image = Image.open("live_demonstration/image/overview.jpeg")
    st.image(image)

st.write("______")

# Add all your applications (sites) here
app.add_page("Overview", project_overview.app)
app.add_page("Live Demonstration", live_demonstration.app)


# The main app
app.run()

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>created by Simon Glauser for Master Thesis</p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)
