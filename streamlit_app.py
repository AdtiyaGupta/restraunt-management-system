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

# Function to view menu
def view_menu(category):
    menu_df = pd.DataFrame(st.session_state.menu[category])
    st.write(menu_df)

# Main application
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", list(st.session_state.menu.keys()))

# Main content
st.title("Menu")
view_menu(selected_menu)
