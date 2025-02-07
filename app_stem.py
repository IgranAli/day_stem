import streamlit as st
import pandas as pd
import numpy as np
 
 # Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")
 
 # Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
     "Go to:",
     ["Researcher Profile", "Publications", "Contact"],)

 
# Dummy Legal Textbooks data
legal_textbooks_data = pd.DataFrame({
    "Title": ["Constitutional Law", "Criminal Procedure", "International Law", "Legal Ethics", "Torts and Liability"],
    "Author": ["John Doe", "Jane Smith", "Emily Johnson", "Michael Lee", "Sarah Davis"],
    "Publication Year": [2020, 2018, 2021, 2019, 2022],
    "ISBN": ["978-1-23456-789-0", "978-0-98765-432-1", "978-1-54321-987-6", "978-0-12345-678-9", "978-1-67890-123-4"],
    "Publisher": ["Oxford University Press", "Cambridge University Press", "Harvard Law Review", "Wiley Law", "Springer Nature"],
    "Date Added": pd.date_range(start="2024-01-01", periods=5),
})

# Print the data to check
print(legal_textbooks_data)

 
 # Sections based on menu selection
if menu =="Researcher Profile":
   st.title("Researcher Profile")
   st.sidebar.header("Profile Options")
 
 # Collect basic information
name = "Dr. Igran Abdi"
field = "Legal Researcher" 
institution = "University of the Western Cape"
 
# Display basic profile information
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}") 

if menu == "Publications":
     st.title("Publications")
     st.sidebar.header("Upload and Filter")
 
     # Upload publications file
     uploaded_file = st.file_uploader("Upload a PDF of Publications", type="pdf")
     if uploaded_file:
         publications = pd.read_csv(uploaded_file)
         st.dataframe(publications)

     
     elif menu == "Contact":
     # Add a contact section
      st.header("Contact Information")
     email = "4249615@myuwc.ac.za"
     st.write(f"You can reach {name} at {email}.")




