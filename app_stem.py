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
 if menu == "Researcher Profile":
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
 
         # Publication trends
         if "Year" in publications.columns:
             st.subheader("Publication Trends")
             year_counts = publications["Year"].value_counts().sort_index()
             st.bar_chart(year_counts)
         else:
             st.write("The CSV does not have a 'Year' column to visualize trends.")
 
 elif menu == "STEM Data Explorer":
     st.title("STEM Data Explorer")
     st.sidebar.header("Data Selection")
 
     # Tabbed view for STEM data
     data_option = st.sidebar.selectbox(
         "Choose a dataset to explore", 
         ["Physics Experiments", "Astronomy Observations", "Weather Data"]
     )
 
     if data_option == "Physics Experiments":
         st.write("### Physics Experiment Data")
         st.dataframe(physics_data)
         # Add widget to filter by Energy levels
         energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
         filtered_physics = physics_data[
             physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
         ]
         st.write(f"Filtered Results for Energy Range {energy_filter}:")
         st.dataframe(filtered_physics)
 
     elif data_option == "Astronomy Observations":
         st.write("### Astronomy Observation Data")
         st.dataframe(astronomy_data)
         # Add widget to filter by Brightness
         brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
         filtered_astronomy = astronomy_data[
             astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
         ]
         st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
         st.dataframe(filtered_astronomy)
 
     elif data_option == "Weather Data":
         st.write("### Weather Data")
         st.dataframe(weather_data)
         # Add widgets to filter by temperature and humidity
         temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
         humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
         filtered_weather = weather_data[
             weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
             weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
         ]
         st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
         st.dataframe(filtered_weather)
 
 elif menu == "Contact":
     # Add a contact section
     st.header("Contact Information")
     email = "4249615@myuwc.ac.za"
     st.write(f"You can reach {name} at {email}.")




