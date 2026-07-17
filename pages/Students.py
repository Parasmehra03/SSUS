import streamlit as st
import pandas as pd

from database.mongodb import student_collection

st.title("📋 Student List")

search = st.text_input("Search Student")

query = {}

if search:
    query = {
        "$or": [
            {
                "first_name": {
                    "$regex": search,
                    "$options": "i"
                }
            },
            {
                "email": {
                    "$regex": search,
                    "$options": "i"
                }
            }
        ]
    }

students = list(student_collection.find(query))

if students:

    for student in students:

        student["_id"] = str(student["_id"])

        # Agar photo Base64 string me store hai
        if student.get("photo"):
            student["photo"] = f"data:image/jpeg;base64,{student['photo']}"
        else:
            student["photo"] = ""

    df = pd.DataFrame(students)

    st.dataframe(
        df,
        column_config={
            "photo": st.column_config.ImageColumn(
                "Photo",
                help="Student Photo"
            )
        },
        hide_index=True,
        use_container_width=True
    )

else:
    st.warning("No Students Found")
