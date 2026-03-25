import streamlit as st
import os
import time

st.set_page_config(page_title="SSC & UPSC Prep", page_icon="📚")

if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🚀 Exam Prep Master 2026")

# --- Sidebar ---
st.sidebar.header("Navigation")
exam_choice = st.sidebar.selectbox("Choose Exam", ["SSC CGL", "UPSC Prelims"])
subject = st.sidebar.radio("Select Subject", ["Polity", "Maths", "History"])

# --- Logic to Load Notes ---
folder_map = {"UPSC Prelims": "upsc", "SSC CGL": "ssc"}
sub_folder = folder_map[exam_choice]

# THIS PART FIXES YOUR ERROR
if subject == "Polity":
    file_name = "president_of_india.md"
elif subject == "Maths":
    file_name = "percentages.md"
else:
    file_name = "history_notes.md"

path = f"content/{sub_folder}/{subject.lower()}/{file_name}"

st.divider()

# --- Display the Notes ---
if os.path.exists(path):
    with open(path, "r") as f:
        st.markdown(f.read())
else:
    st.warning(f"⚠️ Note not found at: `{path}`")
    st.info(f"Make sure you have a file named '{file_name}' in your {subject} folder on GitHub.")

# --- Quiz ---
st.subheader("📝 Quick Check")
if subject == "Polity":
    q, options, correct = "Who is the head of state?", ["PM", "President", "CJI"], "President"
elif subject == "Maths":
    q, options, correct = "What is 10% of 200?", ["10", "20", "30"], "20"
else:
    q, options, correct = "Who founded Maurya Empire?", ["Ashoka", "Chandragupta", "Bindusara"], "Chandragupta"

st.write(f"**Question:** {q}")
user_choice = st.radio("Answer:", options)
if st.button("Submit"):
    if user_choice == correct:
        st.success("Correct!")
        st.session_state.score += 10
    else:
        st.error(f"Incorrect. It is {correct}")
