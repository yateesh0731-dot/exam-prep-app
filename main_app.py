import streamlit as st
import os

st.set_page_config(page_title="Study Vault 2026", page_icon="📚", layout="wide")

# Sidebar - Subject Selection
st.sidebar.title("📑 Subjects")
subject = st.sidebar.selectbox("Choose a Subject", ["Polity", "Maths", "History", "Economy"])

# Sidebar - Subtopic Selection
st.sidebar.divider()
st.sidebar.write(f"**{subject} Topics:**")

if subject == "Polity":
    if subject == "Polity":
    subtopic = st.sidebar.radio("Select Topic", [
        "President of India", 
        "Fundamental Rights", 
        "Directive Principles",
        "Preamble",
        "Parliament",
        "Emergency Provisions",
        "Panchayati Raj"
    ])
elif subject == "Maths":
    subtopic = st.sidebar.radio("Select Topic", ["Percentages", "Ratio and Proportion", "Profit and Loss"])
elif subject == "History":
    subtopic = st.sidebar.radio("Select Topic", ["Indus Valley Civilization", "Vedic Period", "Mughal Empire"])
else:
    subtopic = st.sidebar.radio("Select Topic", ["GDP Concepts", "Inflation", "Banking Sector"])

# Logic to find the file
# This converts "President of India" to "president_of_india.md"
filename = subtopic.lower().replace(" ", "_") + ".md"
path = f"content/{filename}"

# Main Display
st.title(f"{subject}")
st.subheader(f"📝 {subtopic}")
st.divider()

if os.path.exists(path):
    with open(path, "r") as f:
        st.markdown(f.read())
else:
    st.info(f"🚀 **Ready to add notes?** \n\n Create a file named `{filename}` inside your `content` folder on GitHub to see your notes here.")

st.sidebar.divider()
st.sidebar.caption("Last Updated: March 2026")
