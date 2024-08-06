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

if 'orders' not in st.session_state:
    st.session_state.orders = []

# Function to view menu
def view_menu(category):
    menu_df = pd.DataFrame(st.session_state.menu[category])
    st.write(menu_df)

# Function to view orders
def view_orders():
    orders_df = pd.DataFrame(st.session_state.orders)
    st.write(orders_df)

# Main application
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", ['Beverages', 'Chinese', 'North Indian', 'Sweets', 'South Indian', 'Snacks'])

# Menu options
with st.sidebar.expander("Menu Options"):
    pass

# Order management
with st.sidebar.expander("Order Management"):
    pass

# Main content
st.title("Menu")
view_menu(selected_menu)

st.title("Orders")
view_orders()
