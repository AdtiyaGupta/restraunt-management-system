import streamlit as st
import pandas as pd

# Initialize data
if 'menu' not in st.session_state:
    st.session_state.menu = {
        'Beverages': [],
        'Chinese': [],
        'North Indian': [],
        'Sweets': [],
        'South Indian': [],
        'Snacks': []
    }

# Main application
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", ['Beverages', 'Chinese', 'North Indian', 'Sweets', 'South Indian', 'Snacks'])


# Main content
st.title("Menu")
view_menu(selected_menu)

st.title("Orders")
view_orders()
