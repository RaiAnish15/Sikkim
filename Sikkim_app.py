import streamlit as st
import os
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Sikkim Hydrological Dashboard", layout="wide")

# Title
st.title("Hydrological and Meteorological Dashboard - Sikkim")

# Sidebar for dropdown selections
st.sidebar.header("Select Filters")

# Define places
places = ["Singtam", "Rangpo", "Chumthang", "Melli"]

# Define categories
categories = {
    "Water Discharge": ["Daily", "Monthly", "Change"],
    "Meteorological Variables": ["Precipitation", "Temperature"],
    "Analysis": ["CONDITIONAL VOLATILITY","ARIMAX", "LSTM"]
}

# Dropdown for place selection in sidebar
selected_place = st.sidebar.selectbox("Select a place:", ["Select a Place"] + places, index=0)

# Check if a place is selected
if selected_place != "Select a Place":
    # Dropdown for category selection
    selected_category = st.sidebar.selectbox("Select a category:", ["Select a Category"] + list(categories.keys()), index=0)

    if selected_category != "Select a Category":
        # Dropdown for subcategory selection
        selected_subcategory = st.sidebar.selectbox("Select a sub-category:", ["Select a Sub-category"] + categories[selected_category], index=0)

        if selected_subcategory != "Select a Sub-category":
            # Construct file path with "Sikkim" as the main folder
            file_path = f"Sikkim/{selected_place}/{selected_category}/{selected_subcategory}.png"

            # Check if file exists
            if os.path.exists(file_path):
                # Open and resize image
                img = Image.open(file_path)
                fixed_size = (800, 400)  # Set a fixed size (Width x Height)
                img = img.resize(fixed_size)

                # Display resized image
                st.image(img, caption=f"{selected_place} - {selected_subcategory}", use_container_width=True)
            else:
                st.warning("Image not found! Please check if the file exists.")
