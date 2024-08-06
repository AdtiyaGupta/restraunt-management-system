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
st.sidebar.title("Restaurant Management System")

# Menu bar
selected_menu = st.sidebar.selectbox("Select Menu", ['Beverages', 'Chinese', 'North Indian', 'Sweets', 'South Indian', 'Snacks'])

# Menu options
with st.sidebar.expander("Menu Options"):
    add_name = st.text_input("Enter menu item name")
    add_price = st.number_input("Enter price", min_value=0.0)
    if st.button("Add Menu Item"):
        add_menu_item(selected_menu, add_name, add_price)

    delete_name = st.text_input("Enter name of menu item to delete")
    if st.button("Delete Menu Item"):
        delete_menu_item(selected_menu, delete_name)

# Order management
with st.sidebar.expander("Order Management"):
    order_name = st.text_input("Enter name of menu item to order")
    quantity = st.number_input("Enter quantity", min_value=1)
    if st.button("Place Order"):
        place_order(selected_menu, order_name, quantity)

# Main content
st.title("Menu")
view_menu(selected_menu)

st.title("Orders")
view_orders()
