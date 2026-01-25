# bank_System_Project.py

import streamlit as st

# Page configuration
st.set_page_config(page_title="My Bank System", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .banner {
        text-align: center;
        color: #667eea;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    }
    .balance-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
    }
    .balance-box h2 {
        margin: 0;
        font-size: 18px;
    }
    .balance-box h1 {
        margin: 10px 0 0 0;
        font-size: 36px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 0
if 'account_opened' not in st.session_state:
    st.session_state.account_opened = False
if 'name' not in st.session_state:
    st.session_state.name = ""

# Title
st.markdown("""
    <div style="text-align: center;">
    <h1>💰 Welcome to MyBank</h1>
    <p style="color: #666; font-size: 16px;">Your trusted banking partner</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Account Opening Section
if not st.session_state.account_opened:
    st.subheader("📝 Open Your Account")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        name = st.text_input("Enter your name:", placeholder="John Doe")
    
    with col2:
        st.write("")
        st.write("")
        if st.button("Open Account", key="open_btn", use_container_width=True):
            if name.strip():
                st.session_state.name = name
                st.session_state.account_opened = True
                st.success(f"✅ Hey '{name}' Account opened successfully!")
                st.rerun()
            else:
                st.error("⚠️ Please enter your name")

else:
    # Banking Operations Section
    st.markdown(f"<p style='text-align: center; font-size: 18px;'>Welcome, <b>{st.session_state.name}</b>! 👋</p>", unsafe_allow_html=True)
    
    # Show Current Balance
    st.markdown(f"""
    <div class="balance-box">
        <h2>Your Current Balance</h2>
        <h1>${st.session_state.balance:,.2f}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Input amount
    amount = st.number_input("💵 Enter amount:", min_value=0.0, step=0.01, key="amount_input")
    
    st.markdown("---")
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💳 Deposit", use_container_width=True, key="deposit_btn"):
            if amount > 0:
                st.session_state.balance += amount
                st.success(f"✅ Successfully deposited ${amount:,.2f}\nNew balance: ${st.session_state.balance:,.2f}")
                st.rerun()
            else:
                st.error("⚠️ Please enter a valid amount")
    
    with col2:
        if st.button("💸 Withdraw", use_container_width=True, key="withdraw_btn"):
            if amount > 0:
                if st.session_state.balance >= amount:
                    st.session_state.balance -= amount
                    st.success(f"✅ Successfully withdrawn ${amount:,.2f}\nNew balance: ${st.session_state.balance:,.2f}")
                    st.rerun()
                else:
                    st.error(f"❌ Insufficient funds!\nYour balance: ${st.session_state.balance:,.2f}")
            else:
                st.error("⚠️ Please enter a valid amount")
    
    with col3:
        if st.button("❌ Withdraw All", use_container_width=True, key="withdraw_all_btn"):
            if st.session_state.balance > 0:
                withdrawn = st.session_state.balance
                st.session_state.balance = 0
                st.warning(f"⚠️ Withdrawn all ${withdrawn:,.2f}\nNew balance: $0.00")
                st.rerun()
            else:
                st.info("ℹ️ No balance to withdraw")
    
    st.markdown("---")
    
    # Show balance button
    if st.button("📊 Show Balance", use_container_width=True, key="show_balance_btn"):
        st.info(f"💰 Your current balance: ${st.session_state.balance:,.2f}")
    
    # Exit button
    st.markdown("---")
    if st.button("🚪 Exit Account", use_container_width=True, key="exit_btn"):
        st.session_state.account_opened = False
        st.session_state.balance = 0
        st.session_state.name = ""
        st.balloons()
        st.success("👋 Thank you for banking with us. Bye!")
        st.rerun()
