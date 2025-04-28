import streamlit as st
import os
from utils.load_notes import list_courses
from utils.course_wizard import create_new_course

# Page Config
st.set_page_config(
    page_title="Modgul X - Survive Academia",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Light/Dark mode switch
theme = st.sidebar.radio("Pick your vibe", ["Light Mode", "Dark Mode"])
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Logo and Banner
st.image("assets/banner.jpg", use_column_width=True)

st.title("Welcome to **Modgul X**")
st.subheader("Organized chaos, now in **HD** with dark mode.")

st.markdown("""
---

> *"If learning were easy, it would be called Netflix."* — Ancient Modgul X Scrolls.

At Modgul X, you're not just studying — you're **surviving with style**.

Whether you're:
- Procrastinating efficiently
- Actually trying (respect)
- Crying internally

We've got you covered, one mildly passive-aggressive chapter at a time.

---
""")

st.success("**Hint:** Light mode for optimism, dark mode for soul-searching.")

# Sidebar Navigation
st.sidebar.title("Courses Available:")

courses = list_courses()

if not courses:
    st.sidebar.warning("No courses found. 🥲 Add one below!")
else:
    selected_course = st.sidebar.selectbox("Jump to a course:", courses)

    if selected_course:
        st.experimental_set_query_params(course=selected_course)

# Add new course wizard
st.sidebar.markdown("---")
st.sidebar.header("Add New Course")
new_course = st.sidebar.text_input("Enter course name")
if st.sidebar.button("Create Course"):
    result = create_new_course(new_course)
    st.sidebar.success(result)
    st.sidebar.experimental_rerun()

st.markdown("---")
st.header("All Courses:")

cols = st.columns(2)
for idx, course in enumerate(courses):
    with cols[idx % 2]:
        course_display = course.replace('_', ' ').title()
        st.markdown(f"### [{course_display}](./?course={course})")
        st.caption("Dive into chaos, responsibly.")

st.markdown("---")
st.caption("Built with existential dread, but make it cute.")
