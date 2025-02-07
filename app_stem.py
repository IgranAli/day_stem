import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Legal Researcher", layout="wide")

# Define the profile information globally
name = "Ms. Igran Abdi"
field = "Legal"
institution = "University of the Western Cape"
email = "igranaliofficial@gmail.com"

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Choose a section", ["Researcher Profile", "Publications", "Contact"])

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Add the profile picture upload functionality
    profile_pic = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
    
    # Check if the user has uploaded an image
    if profile_pic is not None:
        st.image(profile_pic, caption=name, use_container_width=True)  # Display the uploaded image
    else:
        # If no image uploaded, show a default placeholder or warning
        st.warning("Please upload a profile picture.")
    
    # Create a two-column layout for profile details
    col1, col2 = st.columns([1, 2])
    
    # Add profile details to the second column
    with col2:
        st.write(f"**Name:** {name}")
        st.write(f"**Field of Research:** {field}")
        st.write(f"**Institution:** {institution}")
        st.write(f"**Email:** {email}")
        
        # Short Bio Section
        st.markdown("""
        **Short Bio:**
        Ms. Igran Abdi is a legal researcher with a keen interest in exploring the intersection of law and technology. 
        She is currently pursuing her studies at the University of the Western Cape and aims to contribute to legal advancements 
        in the digital age. Her research focuses on [insert specific areas of research, e.g., AI and ethics, digital privacy laws].
        """)

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
    st.write(f"You can reach {name} at {email}.")
