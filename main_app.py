import streamlit as st
import os

st.set_page_config(page_title="SSC & UPSC Notes", page_icon="📝")

st.title("📚 Combined Study Vault 2026")
st.sidebar.title("Navigation")

# Simplified Selection
subject = st.sidebar.radio("Select Subject", ["Polity", "Maths", "History", "Economy"])

# Path Logic: Everything points to the same 'content' folder now
file_map = {
    "Polity": "polity.md",
    "Maths": "maths.md",
    "History": "history.md",
    "Economy": "economy.md"
}

# The app will now look in: content/polity.md, content/maths.md, etc.
path = f"content/{file_map[subject]}"

st.divider()

if os.path.exists(path):
    with open(path, "r") as f:
        st.markdown(f.read())
else:
    st.info(f"💡 Next Step: On GitHub, create a file named `{file_map[subject]}` inside the `content` folder.")

st.sidebar.divider()
st.sidebar.caption("Bengaluru Prep Mode: ON")
