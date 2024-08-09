import streamlit as st
import pandas as pd

# Initialize data
if 'menu' not in st.session_state:
    st.session_state.menu = {
        'Beverages': [{'Item': 'Cold Coffee', 'Price': 84}, {'Item': 'Hot Coffee', 'Price': 21}, {'Item': 'Sperm Skake','Price': 690}, {'Item': 'Masala Tea','Price': 21}, {'Item': 'Ice Tea','Price': 63}, {'Item': 'Mint Mojito','Price': 84}, {'Item': 'Green Apple Soda','Price': 84}, {'Item': 'Blue Berry','Price': 84}, {'Item': 'Kiwi Punch','Price': 84}, {'Item': 'Mandrine','Price': 84}, {'Item': 'Watermelon Mojito','Price': 84}, {'Item': 'Seasonal Fruit Juice','Price': 84}, {'Item': 'Strawberry Shake','Price': 84}, {'Item': 'Black Current','Price': 84}, {'Item': 'Mango Shake','Price': 84}, {'Item': 'Rose Shake','Price': 84}, {'Item': 'Papaya Shake','Price': 84}, {'Item': 'Banana Shake','Price': 84}, {'Item': 'Kit-Kat Shake','Price': 84}, {'Item': 'Chocolate Shake','Price': 84}, {'Item': 'Oreo Shake','Price': 84}, {'Item': 'Custered Apple Shake','Price': 84}, {'Item': 'Sweet Lassi','Price': 84}, {'Item': 'Mango Lassi','Price': 84}, {'Item': 'Chocolate Lassi','Price': 84}],
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
    """Display menu items for a given category"""
    menu_df = pd.DataFrame(st.session_state.menu[category], columns=['Item', 'Price'])
    st.write(menu_df)

# Function to add item to summary
def add_to_summary(item, category):
    """Add an item to the summary"""
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
    """Remove an item from the summary"""
    st.session_state.summary = [i for i in st.session_state.summary if i['Item'] != item]

# Function to increase item quantity in summary
def increase_quantity(item):
    """Increase the quantity of an item in the summary"""
    for i in st.session_state.summary:
        if i['Item'] == item:
            i['Quantity'] += 1

# Function to decrease item quantity in summary
def decrease_quantity(item):
    """Decrease the quantity of an item in the summary"""
    for i in st.session_state.summary:
        if i['Item'] == item:
            if i['Quantity'] > 1:
                i['Quantity'] -= 1
            else:
                remove_from_summary(item)

# Function to estimate total amount
def estimate_amount():
    """Calculate the estimated total amount"""
    return sum([item['Price'] * item['Quantity'] for item in st.session_state.summary])

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

    # Increase/decrease item quantity
    st.title("Update Quantity")
    update_item_options = [item['Item'] for item in st.session_state.summary]
    selected_update_item = st.selectbox("Select Item to Update", update_item_options)
    if st.button("Increase"):
        increase_quantity(selected_update_item)
    if st.button("Decrease"):
        decrease_quantity(selected_update_item)

    # Estimate amount
    estimated_amount = estimate_amount()
    st.write(f"Estimated Amount: ₹{estimated_amount:.2f}")

    # Place order
    if st.button("Place Order"):
        st.write("Order placed successfully!")
        st.session_state.summary = []  # Clear the summary after placing the
