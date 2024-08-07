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

if 'summary' not in st.session_state:
    st.session_state.summary = []

# Function to view menu
def view_menu(category):
    menu_df = pd.DataFrame(st.session_state.menu[category], columns=['Item'])
    st.write(menu_df)

# Function to add item to summary
def add_to_summary(item, category):
    st.session_state.summary.append({'Item': item, 'Category': category})
    st.experimental_rerun()

# Main application
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", list(st.session_state.menu.keys()))

# Add menu items
st.sidebar.header("Add Menu Items")
with st.sidebar.form("add_item_form"):
    item = st.text_input("Enter item name")
    price = st.number_input("Enter item price")
    submitted = st.form_submit_button("Add Item")
    if submitted:
        st.session_state.menu[selected_menu].append({'Item': item, 'Price': price})

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
estimate_amount = sum([item['Price'] for item in st.session_state.menu[selected_menu] for summary_item in st.session_state.summary if item['Item'] == summary_item['Item']])
st.write(f"Estimated Amount: ${estimate_amount:.2f}")

# Place order
if st.button("Place Order"):
    st.write("Order placed successfully!")
    st.session_state.summary = []
