import streamlit as st

# Title of the dashboard
st.title("Interactive Dashboard")

# Initial dropdown selection with a placeholder
option = st.selectbox("Select an option:", ["Select an option", "Meteorological Details", "Analysis Details"])

# Logic based on selection
if option == "Meteorological Details":
    st.subheader("Select Meteorological Parameters")
    parameter = st.selectbox("Choose a parameter:", ["Select an option", "Daily Discharge","Monthly Discharge","Monthly Change in discharge","Temperature", "Precipitation"])

    # Display the corresponding image based on selection
    if parameter != "Select an option":
        st.image(f"images/{parameter.lower()}.png", caption=f"{parameter} Data", use_column_width=True)

elif option == "Analysis":
    st.subheader("Select Analysis Type")
    analysis_type = st.selectbox("Choose an analysis:", ["Select an option", "Conditional Volatility", "Forecasting using ARIMAX", "Forecasting using LSTM"])

    # Display the corresponding image based on selection
    if analysis_type != "Select an option":
        st.image(f"images/{analysis_type.lower().replace(' ', '_')}.png", caption=f"{analysis_type} Results", use_column_width=True)
