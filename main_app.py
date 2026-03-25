import time
import streamlit as st

st.set_page_config(page_title="SSC & UPSC Prep", page_icon="📚")

# --- Initialize Score in Memory ---
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🚀 Exam Prep Master 2026")

# --- Sidebar ---
st.sidebar.header("Navigation")

# 1. ADDED BACK: The Exam Selection Dropdown
exam_choice = st.sidebar.selectbox("Choose Exam", ["SSC CGL", "UPSC Prelims"])

# 2. Subject Selection
subject = st.sidebar.radio("Select Subject", ["Polity", "Maths", "History"])

# --- Top Statistics Bar ---
col1, col2 = st.columns(2)
col1.metric("Current Score", st.session_state.score)
# This now updates based on your sidebar selection!
col2.metric("Target Exam", exam_choice) 

# --- Dynamic Content Logic ---
if subject == "Polity":
    st.subheader(f"🏛️ Indian Polity ({exam_choice})")
    q = "Who is the 'Guardian' of the Indian Constitution?"
    options = ["President", "Prime Minister", "Supreme Court", "Parliament"]
    correct = "Supreme Court"
elif subject == "Maths":
    st.subheader(f"🔢 Quantitative Aptitude ({exam_choice})")
    q = "A shopkeeper sells an item for ₹120 at a 20% profit. What was the Cost Price?"
    options = ["₹90", "₹100", "₹110", "₹95"]
    correct = "₹100"
else:
    st.subheader(f"📜 Indian History ({exam_choice})")
    q = "Who was the founder of the Maurya Empire?"
    options = ["Ashoka", "Chandragupta Maurya", "Bindusara", "Chanakya"]
    correct = "Chandragupta Maurya"

# --- Quiz Interface ---
st.write(f"**Question:** {q}")
user_choice = st.radio("Select your answer:", options)

if st.button("Check Answer"):
    if user_choice == correct:
        st.balloons()
        st.success("✅ Correct! +10 Points added.")
        st.session_state.score += 10
        time.sleep(2) 
        st.rerun() 
    else:
        st.error(f"❌ Incorrect. The correct answer was {correct}.")

if st.button("Reset Score"):
    st.session_state.score = 0
    st.rerun()

st.divider()
st.subheader("📰 Daily Selection Bulletin")

with st.expander("See Today's Important Facts"):
    st.write("- **Polity:** Article 72 gives the President power to grant pardons.")
    st.write("- **History:** The Dandi March started on March 12, 1930.")
    st.write("- **Maths:** To convert km/hr to m/s, multiply by 5/18.")

st.caption("Updated for 25th March 2026")