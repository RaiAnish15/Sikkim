import streamlit as st
import os

# Get the current directory where the script is located
IMAGE_PATH = os.getcwd()  # Current folder

# Function to load images safely
def load_image(image_name):
    image_file = os.path.join(IMAGE_PATH, image_name)
    if os.path.exists(image_file):
        st.image(image_file, caption=image_name.replace(".png", "").replace("_", " ").title(), use_container_width=True)
    else:
        st.warning(f"Image not found: {image_name}")

# Title of the dashboard
st.title("Sikkim")

# Sidebar with dropdown selection
st.sidebar.header("Options")

# Initial dropdown selection in sidebar
option = st.sidebar.selectbox("Select an option:", ["Select an option", "Meteorological Details", "Analysis Details"])

# Logic based on selection
if option == "Meteorological Details":
    st.sidebar.subheader("Select Meteorological Parameters")
    parameter = st.sidebar.selectbox(
        "Choose a parameter:", 
        ["Select an option", "Daily Discharge", "Monthly Discharge", "Monthly Change in Discharge", "Temperature", "Precipitation"]
    )

    # Display the corresponding image based on selection
    if parameter != "Select an option":
        st.subheader(f"Displaying {parameter} Data")
        image_filename = parameter.lower().replace(" ", "_") + ".png"
        load_image(image_filename)

elif option == "Analysis Details":
    st.sidebar.subheader("Select Analysis Type")
    analysis_type = st.sidebar.selectbox(
        "Choose an analysis:", 
        ["Select an option", "Conditional Volatility", "Forecasting using ARIMAX", "Forecasting using LSTM"]
    )

    # Display the corresponding image based on selection
    if analysis_type != "Select an option":
        st.subheader(f"Displaying {analysis_type} Results")
        image_filename = analysis_type.lower().replace(" ", "_") + ".png"
        load_image(image_filename)
