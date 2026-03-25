import time
import streamlit as st
import os

st.set_page_config(page_title="SSC & UPSC Prep", page_icon="📚")

# --- Initialize Score ---
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🚀 Exam Prep Master 2026")

# --- Sidebar ---
st.sidebar.header("Navigation")
exam_choice = st.sidebar.selectbox("Choose Exam", ["SSC CGL", "UPSC Prelims"])
subject = st.sidebar.radio("Select Subject", ["Polity", "Maths", "History"])

# --- Stats Bar ---
col1, col2 = st.columns(2)
col1.metric("Current Score", st.session_state.score)
col2.metric("Target", exam_choice)

# --- Logic to Load Notes ---
folder_map = {
    "UPSC Prelims": "upsc",
    "SSC CGL": "ssc"
}

# This part is now "smarter" about finding your folders
sub_folder = folder_map[exam_choice]
possible_paths = [
    f"content/{sub_folder}/{subject.lower()}/president_of_india.md",
    f"content/{sub_folder}/{subject}/president_of_india.md",
    f"content/{sub_folder.upper()}/{subject}/president_of_india.md"
]

notes_content = None
for path in possible_paths:
    if os.path.exists(path):
        with open(path, "r") as f:
            notes_content = f.read()
        break

st.divider()

# --- Display the Notes ---
if notes_content:
    st.markdown(notes_content)
else:
    # If the file still isn't found, show this helpful message
    st.warning(f"⚠️ Notes file not found at: `{possible_paths[0]}`")
    st.info("Please ensure your folder on GitHub is named 'content' and contains the 'upsc' folder.")

# --- The Quiz Section ---
st.subheader("📝 Quick Check")
if subject == "Polity":
    q = "Who administers the oath to the President?"
    options = ["PM", "CJI", "VP", "Speaker"]
    correct = "CJI"
# ... (Maths and History logic stays the same) ...
else:
    q = "Who was the founder of Maurya Empire?"
    options = ["Ashoka", "Chandragupta Maurya", "Bindusara", "Chanakya"]
    correct = "Chandragupta Maurya"

user_choice = st.radio("Your Answer:", options)

if st.button("Submit"):
    if user_choice == correct:
        st.balloons()
        st.success("Correct!")
        st.session_state.score += 10
        time.sleep(1)
        st.rerun()
    else:
        st.error(f"Wrong! It was {correct}")

# --- Daily News ---
st.divider()
st.caption("Updated for Bengaluru Students - March 2026")
