import os

def create_new_course(course_name, notes_dir="notes"):
    course_path = os.path.join(notes_dir, course_name.replace(' ', '_'))

    if not os.path.exists(course_path):
        os.makedirs(course_path)
        # Create some starter chapters
        for i in range(1, 4):
            with open(os.path.join(course_path, f"chapter{i}.md"), "w", encoding="utf-8") as f:
                f.write(f"# Chapter {i}\n\nWelcome to Chapter {i} of {course_name}.\n\nStay confused, stay learning.")
        return f"Course '{course_name}' created with starter chapters!"
    else:
        return f"Course '{course_name}' already exists!"
