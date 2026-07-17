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
            student["photo"] = "data:image/Jpeg;base64," + base64.b64decode(student["photo"]).decode("latin")
        else:
            student["photo"] = ""
    

    df = pd.DataFrame(students)

    img = JsCode("""
    class ImgRenderer{
        init(params){
            this.eGui=document.createElement('img');
            this.eGui.src=params.value;
            this.eGui.width=60;
            this.eGui.height=60;
        }
        getGui(){
            return this.eGui;
        }
    }
    """)

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
