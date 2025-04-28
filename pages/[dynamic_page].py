import streamlit as st
from utils.load_notes import list_chapters, load_chapter_content

# Get course from URL
query_params = st.experimental_get_query_params()
course_name = query_params.get("course", [None])[0]

if course_name:
    course_display = course_name.replace("_", " ")
    st.set_page_config(
        page_title=f"{course_display} - Modgul X",
        page_icon=":books:",
        layout="wide",
    )
    st.title(f"Course: {course_display}")
    
    chapters = list_chapters(course_name)

    if not chapters:
        st.warning("No chapters here yet. It's just you and your dreams.")
    else:
        chapter = st.selectbox("Pick a chapter:", chapters)

        content = load_chapter_content(course_name, chapter)
        st.markdown("---")
        st.markdown(content)
        st.markdown("---")
        st.caption("We don't judge how many times you re-read Chapter 1.")
else:
    st.warning("No course selected. Go back to the homepage and pretend you have a plan.")
