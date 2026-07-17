import streamlit as st
import pandas as pd
import base64


from database.mongodb import student_collection

st.title("📋 Student List")

search = st.text_input(
    "Search Student"
)

query = {}

if search:

    query = {

        "$or":[

            {
                "first_name":{
                    "$regex":search,
                    "$options":"i"
                }
            },

            {
                "email":{
                    "$regex":search,
                    "$options":"i"
                }
            }
        ]
    }

students = list(
    student_collection.find(query)
)

if students:

    for student in students:

        student["_id"] = str(student["_id"])

        if student.get("photo"):
            img_bytes = bytes(student["photo"])
            student["photo"] = (
                "data:image/jpeg;base64, "
                + base64.b64encode(img_bytes).decode("uff-8")
            )
        else:
            student["photo"] = ""
    

    df = pd.DataFrame(students)



    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_column(
        "photo",
        cellRenderer=img
    )

    gridOptions = gb.build()

    AgGrid(
        df,
        gridOptions=gridOptions,
        allow_unsafe_jscode=True
    )



else:

    st.warning(
        "No Students Found"
    )
