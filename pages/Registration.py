import streamlit as st

from database.mongodb import student_collection

st.title("Student Registration")

first_name = st.text_input("First Name")

last_name = st.text_input("Last Name")

email = st.text_input("Email")

course = st.text_input("Course")

photo = st.file_uploader(
    "Upload Student Photo",
    type=["jpg", "jpeg", "png"]
)

if photo is not None:
    st.image(
        photo,
        width=150,
        caption="Student Photo"
    )


if st.button("Register Student"):

    if not first_name or not last_name or not email or not course:

        st.error("Please fill all fields")

    elif photo is None:

        st.error("Please upload student photo")

    else:

        photo_data = photo.read()

        student_collection.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "course": course,
            "photo": photo_data
        })

        st.success("Student Registered Successfully")
