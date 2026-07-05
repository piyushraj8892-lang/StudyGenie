import streamlit as st
from ai import generate_work

st.title("🎓 StudyGenie AI")

grade = st.selectbox(
    "Select Class",
    ["5","6","7","8","9","10","11","12"]
)

subject = st.text_input("Subject")

task = st.selectbox(
    "Task Type",
    [
        "Homework",
        "Assignment",
        "Project",
        "Essay"
    ]
)

topic = st.text_input("Topic")

if st.button("Generate"):

    result = generate_work(
        grade,
        subject,
        task,
        topic
    )

    st.write(result)
