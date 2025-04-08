import streamlit as st
import numpy as np

st.title("🧠 In-Memory CRUD App (No DB, NumPy Only)")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = np.array([["Alice", "alice@example.com"]], dtype=object)

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Action", menu)

def add_user(name, email):
    new_entry = np.array([[name, email]], dtype=object)
    st.session_state.data = np.vstack([st.session_state.data, new_entry])

def update_user(index, name, email):
    st.session_state.data[index] = [name, email]

def delete_user(index):
    st.session_state.data = np.delete(st.session_state.data, index, axis=0)

if choice == "Create":
    st.subheader("➕ Add New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Add"):
        if name and email:
            add_user(name, email)
            st.success("User added successfully!")
        else:
            st.warning("Both fields are required.")

elif choice == "Read":
    st.subheader("📖 View Users")
    if st.session_state.data.shape[0] == 0:
        st.info("No users yet.")
    else:
        for i, (name, email) in enumerate(st.session_state.data):
            st.write(f"**{i+1}.** {name} | {email}")

elif choice == "Update":
    st.subheader("✏️ Update User")
    if st.session_state.data.shape[0] == 0:
        st.info("No users to update.")
    else:
        user_index = st.selectbox("Select User", range(len(st.session_state.data)),
                                  format_func=lambda i: f"{i+1}. {st.session_state.data[i][0]}")
        name = st.text_input("New Name", value=st.session_state.data[user_index][0])
        email = st.text_input("New Email", value=st.session_state.data[user_index][1])
        if st.button("Update"):
            update_user(user_index, name, email)
            st.success("User updated successfully.")

elif choice == "Delete":
    st.subheader("🗑️ Delete User")
    if st.session_state.data.shape[0] == 0:
        st.info("No users to delete.")
    else:
        user_index = st.selectbox("Select User", range(len(st.session_state.data)),
                                  format_func=lambda i: f"{i+1}. {st.session_state.data[i][0]}")
        if st.button("Delete"):
            delete_user(user_index)
            st.warning("User deleted.")

