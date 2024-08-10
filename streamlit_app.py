import streamlit as st
import pandas as pd
import random

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


config = {
    "toImageButtonOptions": {
        "format": "png",
        "filename": "custom_image",
        "height": 720,
        "width": 480,
        "scale": 6,
    }
}

icons = {
    "assistant": "https://raw.githubusercontent.com/sahirmaharaj/exifa/2f685de7dffb583f2b2a89cb8ee8bc27bf5b1a40/img/assistant-done.svg",
    "user": "https://raw.githubusercontent.com/sahirmaharaj/exifa/2f685de7dffb583f2b2a89cb8ee8bc27bf5b1a40/img/user-done.svg",
}

particles_js = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }
  
</style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 300,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#ffffff"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#ffffff",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""

st.set_page_config(page_title="Exifa.net", page_icon="✨", layout="wide")




# Function to view menu
def view_menu(category):
    """Display menu items for a given category"""
    menu_df = pd.DataFrame(st.session_state.menu[category], columns=['Item', 'Price'])
    num_cols = 3
    num_rows_per_col = 10
    cols = st.columns(num_cols)
    for i, row in menu_df.iterrows():
        col_idx = i % num_cols
        row_idx = i // num_cols
        if row_idx >= num_rows_per_col:
            break
        with cols[col_idx]:
            st.write(f"{row['Item']} - ₹{row['Price']}")
    
   
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
