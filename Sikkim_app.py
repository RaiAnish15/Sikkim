import streamlit as st
import os

# Get the current directory where the script is located
IMAGE_PATH = os.getcwd()  # Current folder

# Function to load images safely
def load_image(image_name):
    image_file = os.path.join(IMAGE_PATH, image_name)
    if os.path.exists(image_file):
        st.image(image_file, caption=image_name.replace(".png", "").replace("_", " ").title(), use_column_width=True)
    else:
        st.warning(f"Image not found: {image_name}")

# Title of the dashboard
st.title("Interactive Dashboard")

# Initial dropdown selection with a placeholder
option = st.selectbox("Select an option:", ["Select an option", "Meteorological Details", "Analysis Details"])

# Logic based on selection
if option == "Meteorological Details":
    st.subheader("Select Meteorological Parameters")
    parameter = st.selectbox(
        "Choose a parameter:", 
        ["Select an option", "Daily Discharge", "Monthly Discharge", "Monthly Change in Discharge", "Temperature", "Precipitation"]
    )

    # Display the corresponding image based on selection
    if parameter != "Select an option":
        image_filename = parameter.lower().replace(" ", "_") + ".png"
        load_image(image_filename)

elif option == "Analysis Details":
    st.subheader("Select Analysis Type")
    analysis_type = st.selectbox(
        "Choose an analysis:", 
        ["Select an option", "Conditional Volatility", "Forecasting using ARIMAX", "Forecasting using LSTM"]
    )

    # Display the corresponding image based on selection
    if analysis_type != "Select an option":
        image_filename = analysis_type.lower().replace(" ", "_") + ".png"
        load_image(image_filename)
