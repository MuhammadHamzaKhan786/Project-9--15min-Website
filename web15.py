# Project 9 Build a Python Website in 15 min With Streamlit


import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data  Generator", page_icon=":guardsman:", layout="wide")
st.title("Student CSV FileGenerator")

name = ["Hamza", "Ali", "Sara", "Aisha", "Omar", "Fatima", "Zain", "Hassan", "Yasmin", "Bilal"]
surname = ["Khan", "Ali", "Ahmed", "Hussain", "Iqbal", "Shaikh", "Syed", "Farooq", "Raza", "Memon"]

students = []
for i in range(1,16):
    student = {
        "Student ID": i,
        "Name": random.choice(name),
        "Surname": random.choice(surname),
        "Age": random.randint(18, 25),
        "Gender": random.choice(["Male", "Female"])
        "Grade": random.choice(["A", "B", "C", "D", "E"]),
        "Marks": random.randint(50, 100),
        "Attendance": random.randint(0, 100),
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generated Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv_file,
    file_name="student_data.csv",
    mime="text/csv",
)
st.success("CSV file generated successfully!")

    
