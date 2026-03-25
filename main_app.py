import streamlit as st
import os

st.set_page_config(page_title="SSC & UPSC Vault", page_icon="📑", layout="wide")

st.title("📚 Combined Study Vault 2026")

# 1. Select Main Subject
subject = st.sidebar.selectbox("Select Subject", ["Polity", "Maths", "History", "Economy"])

# 2. Define Subtopics for each Subject
if subject == "Polity":
    subtopic = st.sidebar.radio("Topic", ["President of India", "Fundamental Rights", "Fundamental Duties"])
    file_name = subtopic.lower().replace(" ", "_") + ".md"
elif subject == "Maths":
    subtopic = st.sidebar.radio("Topic", ["Percentages", "Ratio and Proportion", "Profit and Loss"])
    file_name = subtopic.lower().replace(" ", "_") + ".md"
elif subject == "History":
    subtopic = st.sidebar.radio("Topic", ["Indus Valley Civilization", "Mughal Empire", "Revolt of 1857"])
    file_name = subtopic.lower().replace(" ", "_") + ".md"
else:
    subtopic = st.sidebar.radio("Topic", ["GDP and National Income", "Inflation", "Banking"])
    file_name = subtopic.lower().replace(" ", "_") + ".md"

# 3. Path Logic
# Files must be inside 'content' folder on GitHub
path = f"content/{file_name}"

st.subheader(f"📖 {subtopic}")
st.divider()

# 4. Display Content
if os.path.exists(path):
    with open(path, "r") as f:
        st.markdown(f.read())
else:
    st.warning(f"File not found!")
    st.info(f"To see notes here, create a file named `{file_name}` in your GitHub `content` folder.")
