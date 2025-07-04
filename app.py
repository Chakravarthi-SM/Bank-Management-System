import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

# Initialize session state to track selected page
if "page" not in st.session_state:
    st.session_state.page = "Create Account"

# Sidebar Buttons (look like navbar buttons)
st.sidebar.title("🔗 Operations")
if st.sidebar.button("➕ Create Account"):
    st.session_state.page = "Create Account"
if st.sidebar.button("💸 Deposit"):
    st.session_state.page = "Deposit"
if st.sidebar.button("🏧 Withdraw"):
    st.session_state.page = "Withdraw"
if st.sidebar.button("👁️ View Details"):
    st.session_state.page = "View Details"
if st.sidebar.button("📝 Update Details"):
    st.session_state.page = "Update Details"
if st.sidebar.button("🗑️ Delete Account"):
    st.session_state.page = "Delete Account"

# --------------------
# Main Content Section
# --------------------

# ✅ 1. Create Account
if st.session_state.page == "Create Account":
    st.subheader("➕ Create New Bank Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email Address")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if name and email and pin:
            result = bank.create_account(name, age, email, int(pin))
            if "success" in result:
                st.success(result["success"])
                st.json(result["account"])
            else:
                st.error(result["error"])
        else:
            st.warning("Please fill all fields.")

# ✅ 2. Deposit
elif st.session_state.page == "Deposit":
    st.subheader("💸 Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to Deposit", step=100)

    if st.button("Deposit"):
        result = bank.deposit(acc_no, int(pin), amount)
        if "success" in result:
            st.success(result["success"])
            st.info(f"New Balance: ₹{result['balance']}")
        else:
            st.error(result["error"])

# ✅ 3. Withdraw
elif st.session_state.page == "Withdraw":
    st.subheader("🏧 Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to Withdraw", step=100)

    if st.button("Withdraw"):
        result = bank.withdraw(acc_no, int(pin), amount)
        if "success" in result:
            st.success(result["success"])
            st.info(f"Remaining Balance: ₹{result['balance']}")
        else:
            st.error(result["error"])

# ✅ 4. View Details
elif st.session_state.page == "View Details":
    st.subheader("👁️ Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Get Details"):
        result = bank.show_details(acc_no, int(pin))
        if "error" in result:
            st.error(result["error"])
        else:
            st.json(result)

# ✅ 5. Update Details
elif st.session_state.page == "Update Details":
    st.subheader("📝 Update Your Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (leave blank to skip)")
    email = st.text_input("New Email (leave blank to skip)")
    new_pin = st.text_input("New 4-digit PIN (optional)")

    if st.button("Update"):
        result = bank.update_details(acc_no, int(pin), name or None, email or None, new_pin or None)
        if "success" in result:
            st.success(result["success"])
            st.json(result["user"])
        else:
            st.error(result["error"])

# ✅ 6. Delete Account
elif st.session_state.page == "Delete Account":
    st.subheader("🗑️ Delete Your Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        result = bank.delete_account(acc_no, int(pin))
        if "success" in result:
            st.success(result["success"])
        else:
            st.error(result["error"])
