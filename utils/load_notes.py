import os

def list_courses(notes_dir="notes"):
    return [course for course in os.listdir(notes_dir) if os.path.isdir(os.path.join(notes_dir, course))]

def list_chapters(course, notes_dir="notes"):
    course_path = os.path.join(notes_dir, course)
    if not os.path.exists(course_path):
        return []
    return sorted([chapter for chapter in os.listdir(course_path) if chapter.endswith(".md")])

def load_chapter_content(course, chapter, notes_dir="notes"):
    chapter_path = os.path.join(notes_dir, course, chapter)
    if not os.path.exists(chapter_path):
        return "Oops. This chapter is still brewing its existential crisis. Check back later!"
    with open(chapter_path, "r", encoding="utf-8") as f:
        return f.read()
