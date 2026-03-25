import streamlit as st
import os

# 1. Page Config
st.set_page_config(page_title="My Exam Vault", page_icon="📖", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("📚 Study Vault")
exam_choice = st.sidebar.selectbox("Exam Type", ["UPSC Prelims", "SSC CGL"])
subject = st.sidebar.radio("Subject", ["Polity", "Maths", "History", "Economy"])

# 3. Simple Path Logic
folder_map = {"UPSC Prelims": "upsc", "SSC CGL": "ssc"}
file_map = {
    "Polity": "president_of_india.md",
    "Maths": "percentages.md",
    "History": "history_notes.md"
    "Economy": "economy_notes.md"
}

path = f"content/{folder_map[exam_choice]}/{subject.lower()}/{file_map[subject]}"

# 4. Main Display Area
st.title(f"{subject} Notes")
st.caption(f"Currently viewing: {exam_choice}")
st.divider()

if os.path.exists(path):
    with open(path, "r") as f:
        st.markdown(f.read())
else:
    st.info(f"📁 To add notes here, upload a file to GitHub at: `{path}`")

# 5. Footer
st.sidebar.divider()
st.sidebar.info("Tip: Use the sidebar to switch between subjects instantly.")
