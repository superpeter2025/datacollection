import streamlit as st
import pandas as pd
import os

# File to store user data
DATA_FILE = "user_data.csv"

# Initialize or load user data
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Name", "Email", "Age", "Comments"]).to_csv(DATA_FILE, index=False)

# Streamlit app
st.title("User Information Collection App")

# Input fields for user information
st.header("Please enter your information:")
name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=1, step=1)
comments = st.text_area("Comments")

# Button to submit data
if st.button("Submit"):
    if name and email and age:
        # Save user information to CSV file
        new_data = pd.DataFrame([[name, email, age, comments]], columns=["Name", "Email", "Age", "Comments"])
        new_data.to_csv(DATA_FILE, mode="a", header=False, index=False)
        st.success("Your information has been submitted successfully!")
    else:
        st.error("Please fill in all required fields.")

# Button to download all user data as Excel
if st.button("Download All Data as Excel"):
    if os.path.exists(DATA_FILE):
        # Read the data file
        user_data = pd.read_csv(DATA_FILE)
        # Save to an Excel file
        excel_file = "user_data.xlsx"
        user_data.to_excel(excel_file, index=False, engine="openpyxl")
        # Provide download link
        with open(excel_file, "rb") as file:
            st.download_button(
                label="Download Excel File",
                data=file,
                file_name="user_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("No data available to download yet.")

# Display all user data
st.header("All User Data:")
if os.path.exists(DATA_FILE):
    user_data = pd.read_csv(DATA_FILE)
    st.dataframe(user_data)
else:
    st.write("No data available.")
