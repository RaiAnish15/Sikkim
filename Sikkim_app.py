import streamlit as st
import os

# Set title
st.title("Hydrological and Meteorological Dashboard - Sikkim")

# Define places
places = ["Singtam", "Rangpo", "Chumthang", "Melli"]

# Define categories
categories = {
    "Water Discharge": ["Daily", "Monthly", "Change"],
    "Meteorological Variables": ["Precipitation", "Temperature"],
    "Analysis": ["CONDITIONAL VOLATILITY","ARIMAX", "LSTM"]
}

# Dropdown for place selection
selected_place = st.selectbox("Select a place:", places)

# Dropdown for category selection
selected_category = st.selectbox("Select a category:", list(categories.keys()))

# Dropdown for subcategory selection
selected_subcategory = st.selectbox("Select a sub-category:", categories[selected_category])

# Construct file path with "Sikkim" as the main folder
file_path = f"Sikkim/{selected_place}/{selected_category}/{selected_subcategory}.png"

# Display the selected image
if os.path.exists(file_path):
    st.image(file_path, caption=f"{selected_place} - {selected_subcategory}", use_column_width=True)
else:
    st.warning("Image not found! Please check if the file exists.")

