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

# Function to add menu item
def add_menu_item(category, name, price):
    new_item = {
        'Name': name,
        'Price': price
    }
    st.session_state.menu[category].append(new_item)

# Function to view menu
def view_menu(category):
    menu_df = pd.DataFrame(st.session_state.menu[category])
    st.write(menu_df)

# Function to delete menu item
def delete_menu_item(category, name):
    for item in st.session_state.menu[category]:
        if item['Name'] == name:
            st.session_state.menu[category].remove(item)
            break

# Function to place order
def place_order(category, name, quantity):
    for item in st.session_state.menu[category]:
        if item['Name'] == name:
            new_order = {
                'Name': name,
                'Quantity': quantity,
                'Price': item['Price'] * quantity
            }
            st.session_state.orders.append(new_order)
            break

# Function to view orders
def view_orders():
    orders_df = pd.DataFrame(st.session_state.orders)
    st.write(orders_df)

# Main application
st.title("Restaurant Management System")

# Menu bar
st.header("Menu")
selected_menu = st.selectbox("Select Menu", ['Beverages', 'Chinese', 'North Indian', 'Sweets', 'South Indian', 'Snacks'])

# Add menu item
st.header("Add Menu Item")
add_col1, add_col2 = st.columns(2)
with add_col1:
    name = st.text_input("Enter menu item name")
    price = st.number_input("Enter price", min_value=0.0)
with add_col2:
    if st.button("Add Menu Item"):
        add_menu_item(selected_menu, name, price)

# View menu
if st.button("View Menu"):
    view_menu(selected_menu)

# Delete menu item
delete_name = st.text_input("Enter name of menu item to delete")
if st.button("Delete Menu Item"):
    delete_menu_item(selected_menu, delete_name)

# Order management
st.header("Order Management")
order_col1, order_col2 = st.columns(2)
with order_col1:
    order_name = st.text_input("Enter name of menu item to order")
    quantity = st.number_input("Enter quantity", min_value=1)
with order_col2:
    if st.button("Place Order"):
        place_order(selected_menu, order_name, quantity)

# View orders
if st.button("View Orders"):
    view_orders()
