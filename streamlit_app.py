import streamlit as st
import pandas as pd

# Initialize data
if 'menu' not in st.session_state:
    st.session_state.menu = {
        'Beverages': [{'Item': 'Cold Coffee', 'Price': 84}, {'Item': 'Hot Coffee', 'Price': 70}],
        'Chinese': [{'Item': 'Veg Fried Rice', 'Price': 120}, {'Item': 'Chicken Fried Rice', 'Price': 150}],
        'North Indian': [{'Item': 'Chana Masala', 'Price': 100}, {'Item': 'Palak Paneer', 'Price': 120}],
        'Sweets': [{'Item': 'Gulab Jamun', 'Price': 80}, {'Item': 'Jalebi', 'Price': 90}],
        'South Indian': [{'Item': 'Idli', 'Price': 60}, {'Item': 'Dosa', 'Price': 80}],
        'Snacks': [{'Item': 'Samosa', 'Price': 50}, {'Item': 'Pakora', 'Price': 60}]
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
            existing_item = next((i for i in st.session_state.summary if i['Item'] == item), None)
            if existing_item:
                existing_item['Quantity'] += 1
            else:
                menu_item['Quantity'] = 1
                st.session_state.summary.append(menu_item.copy())  # Create a copy of the menu item

# Function to remove item from summary
def remove_from_summary(item):
    st.session_state.summary = [i for i in st.session_state.summary if i['Item'] != item]

# Function to increase item quantity in summary
def increase_quantity(item):
    for i in st.session_state.summary:
        if i['Item'] == item:
            i['Quantity'] += 1

# Function to decrease item quantity in summary
def decrease_quantity(item):
    for i in st.session_state.summary:
        if i['Item'] == item:
            if i['Quantity'] > 1:
                i['Quantity'] -= 1
            else:
                remove_from_summary(item)

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
    st.experimental_rerun()

# Summary
st.title("Summary")
if st.session_state.summary:
    summary_df = pd.DataFrame(st.session_state.summary)
    summary_df['Total'] = summary_df.apply(lambda row: row['Price'] * row['Quantity'], axis=1)
    st.write(summary_df)

    # Remove item from summary
    st.title("Remove Item")
    remove_item_options = [item['Item'] for item in st.session_state.summary]
    selected_remove_item = st.selectbox("Select Item to Remove", remove_item_options)
    if st.button("Remove"):
        remove_from_summary(selected_remove_item)
        st.experimental_rerun()

    # Increase/decrease item quantity
    st.title("Update Quantity")
    update_item_options = [item['Item'] for item in st.session_state.summary]
    selected_update_item = st.selectbox("Select Item to Update", update_item_options)
    if st.button("Increase"):
        increase_quantity(selected_update_item)
        summary_df = pd.DataFrame(st.session_state.summary)
        summary_df['Total'] = summary_df.apply(lambda row: row['Price'] * row['Quantity'], axis=1)
        st.write(summary_df)
        st.experimental_rerun()
    if st.button("Decrease"):
        decrease_quantity(selected_update_item)
        summary_df = pd.DataFrame(st.session_state.summary)
        summary_df['Total'] = summary_df.apply(lambda row: row['Price'] * row['Quantity'], axis=1)
        st.write(summary_df)
        st.experimental_rerun()

    # Estimate amount
    estimate_amount = sum([item['Price'] * item['Quantity'] for item in st.session_state.summary])
    st.write(f"Estimated Amount: ₹{estimate_amount:.2f}")

    # Place order
    if st.button("Place Order"):
        st.write("Order placed successfully!")
        st.session_state.summary = []
        st.experimental_rerun()
else:
    st.write("No items in summary.")
