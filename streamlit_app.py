import streamlit as st
import pandas as pd

# Initialize data
if 'menu' not in st.session_state:
    st.session_state.menu = {
        'Beverages': [{'Item': 'Cold Coffee', 'Price': 84}, {'Item': 'Hot Coffee', 'Price': 70}],
        'Chinese': [{'Item': 'Veg Fried Rice', 'Price': 120}, {'Item': 'Chicken Fried Rice', 'Price': 150}],
        'North Indian': [{'Item': 'Chana Masala', 'Price': 100}, {'Item': 'Palak Paneer', 'Price': 120}],
        'Sweets': [{'Item': 'Gulab Jamun', 'Price': 80}, {'Item': 'Jalebi', 'Price': 90}],
        'South Indian': [{'Item': 'Idli', 'Price': 60}, {'Item': 'Dosa', 'Price': 84}],
        'Snacks': [{'Item': 'Samosa', 'Price': 32}, {'Item': 'Pakora', 'Price': 60}]
    }

if 'summary' not in st.session_state:
    st.session_state.summary = []

# Function to view menu
def view_menu(category):
    menu_df = pd.DataFrame(st.session_state.menu[category], columns=['Item', 'Price'])
    st.write(menu_df)

# Function to add item to summary
def add_to_summary(item, category):
    for menu_item in st.session_state.menu[category]:
        if menu_item['Item'] == item:
            st.session_state.summary.append(menu_item)
            st.experimental_rerun()

# Main application
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", list(st.session_state.menu.keys()))

# Main content
st.title("Menu")
view_menu(selected_menu)

# Select menu item
st.title("Select Item")
item_list = st.session_state.menu[selected_menu]
item_options = [item['Item'] for item in item_list]
selected_item = st.selectbox("Select Item", item_options)
if st.button("Add to Summary"):
    add_to_summary(selected_item, selected_menu)

# Summary
st.title("Summary")
summary_df = pd.DataFrame(st.session_state.summary)
st.write(summary_df)

# Estimate amount
estimate_amount = sum([item['Price'] for item in st.session_state.summary])
st.write(f"Estimated Amount: ₹{estimate_amount:.2f}")

# Place order
if st.button("Place Order"):
    st.write("Order placed successfully!")
    st.session_state.summary = []
