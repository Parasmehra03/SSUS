import streamlit as st

st.title("Student Registration")

first_name = st.text_input(
    "First Name"
)

last_name = st.text_input(
    "Last Name"
)

email = st.text_input(
    "Email"
)

course = st.text_input(
    "Course"
)

# Photo Upload
photo = st.file_uploader(
    "Upload Student Photo",
    type=["jpg", "jpeg", "png"]
)

# Photo Preview
if photo is not None:
    st.image(photo, width=150, caption="Student Photo")

if st.button("Register Student"):

    photo_data = None

    if photo is not None:
        photo_data = photo.read()

    student_collection.insert_one({

        "first_name": first_name,

        "last_name": last_name,

        "email": email,

        "course": course,

        "photo": photo_data

    })

    st.success("Student Registered Successfully")