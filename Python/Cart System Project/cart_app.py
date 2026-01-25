import streamlit as st

# Session cart storage (persistent per user session)
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Page UI settings
st.set_page_config(page_title="Shopping Cart System", page_icon="🛒", layout="centered")

st.title("🛒 Online Cart System")
st.write("Add, update, remove or buy items with a clean interactive UI.")

# ---------- Functions ----------
def add_item(product, qty):
    st.session_state.cart[product] = qty

def update_item(product, qty):
    st.session_state.cart[product] = qty

def remove_item(product):
    st.session_state.cart.pop(product, None)


# ---------- Sidebar Reset ----------
st.sidebar.header("⚙️ Options")
if st.sidebar.button("Reset Cart"):
    st.session_state.cart = {}
    st.sidebar.success("Cart cleared!")


# ---------- Add Section ----------
with st.expander("➕ Add Product"):
    p_name = st.text_input("Product Name")
    p_qty = st.number_input("Quantity", min_value=1, step=1, value=1)

    if st.button("Add to Cart"):
        if p_name.strip():
            add_item(p_name.strip(), p_qty)
            st.success(f"{p_qty}× {p_name} added.")
        else:
            st.warning("Enter a valid product name!")


# ---------- Update Section ----------
with st.expander("✏️ Update Product"):
    u_name = st.text_input("Enter product to update")
    u_qty = st.number_input("New Quantity", min_value=0, step=1, value=1)

    if st.button("Update Item"):
        if u_name.strip():
            update_item(u_name.strip(), u_qty)
            st.success(f"{u_name} updated to {u_qty}.")
        else:
            st.warning("Enter a product name to update!")


# ---------- Remove Section ----------
with st.expander("❌ Remove Product"):
    r_name = st.text_input("Enter product to remove")

    if st.button("Remove Item"):
        if r_name.strip():
            remove_item(r_name.strip())
            st.success(f"{r_name} removed (if it existed).")
        else:
            st.warning("Enter a valid product to remove!")


# ---------- Display Cart ----------
st.subheader("🛍 Current Cart")

if st.session_state.cart:
    items = [{"Product": p, "Quantity": q} for p, q in st.session_state.cart.items()]
    st.table(items)
else:
    st.info("Your cart is empty — add something 😄")


# ---------- Checkout ----------
if st.button("🛒 Buy & Checkout"):
    if st.session_state.cart:
        st.success("Purchase completed successfully 🎉 — Thank you!")
        st.session_state.cart = {}
    else:
        st.warning("Cart is empty! Add items first.")


st.caption("Made by Sayed Hamza❤️")