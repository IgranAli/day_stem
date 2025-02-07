import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Legal Researcher", layout="wide")

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

# Collect basic information
name = "Ms. Igran Abdi"
field = "Legal"
institution = "University of the Western Cape"

# Display basic profile information
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

elif menu == "Publications":
st.title("Publications")
st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

    

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "igranaliofficial@gmail.com"
    st.write(f"You can reach {name} at {email}.")



