import streamlit as st

st.title("Student Registration")

first_name = st.text_input("First Name")

last_name = st.text_input("Last Name")

email = st.text_input("Email")

course = st.text_input("Course")


if st.button("Register Student"):

    if first_name and last_name and email and course:

        st.success("Student Registered Successfully")

        st.write("First Name:", first_name)
        st.write("Last Name:", last_name)
        st.write("Email:", email)
        st.write("Course:", course)

    else:
        st.error("Please fill all fields")
