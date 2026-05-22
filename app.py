# ========================
# Imports
# ========================

import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

# ========================
# Data Persistence
# ========================

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

st.set_page_config(page_title="Kickflip Quest", page_icon="🛹")

if "tricks" not in st.session_state:
    st.session_state.tricks = load_data()

st.title("🛹 Kickflip Quest")
st.write("Track skate tricks, practice progress, notes, videos, and reference links.")

# ========================
# Sidebar Navigation
# ========================

page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Add Trick", "Practice Log", "Dashboard"]
)

if page == "Home":
    st.header("Welcome")
    st.write("Use this app to track your skateboarding progress over time.")
# ========================
# Add Trick Page
# ========================

elif page == "Add Trick":
    st.header("Add a Trick")

    name = st.text_input("Trick name")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    goal = st.text_input("Goal", placeholder="Example: Land 5 clean kickflips")

    if st.button("Save Trick"):
        if name:
            st.session_state.tricks[name] = {
                "difficulty": difficulty,
                "goal": goal,
                "attempts": 0,
                "landed": 0,
                "notes": [],
                "youtube_links": [],
                "history": []
            }
            save_data(st.session_state.tricks)
            st.success(f"{name} saved!")
        else:
            st.warning("Please enter a trick name.")

# ========================
# Practice Log Page
# ========================

elif page == "Practice Log":
    st.header("Practice Log")

    if not st.session_state.tricks:
        st.write("Add a trick first.")
    else:
        selected_trick = st.selectbox(
            "Choose trick",
            list(st.session_state.tricks.keys())
        )

        session_date = st.date_input("Practice date")

        attempts = st.number_input("Attempts today", min_value=0, step=1)
        landed = st.number_input("Landed today", min_value=0, step=1)
        note = st.text_area("Practice notes")
        youtube_link = st.text_input("YouTube reference link")

        uploaded_video = st.file_uploader(
            "Upload practice video",
            type=["mp4", "mov"]
        )

        if uploaded_video:
            st.video(uploaded_video)

        if st.button("Save Practice Session"):
            trick = st.session_state.tricks[selected_trick]

            trick["attempts"] += attempts
            trick["landed"] += landed

            if note:
                trick["notes"].append(note)

            if youtube_link:
                trick["youtube_links"].append(youtube_link)

            if "history" not in trick:
                trick["history"] = []

            trick["history"].append({
                "date": str(session_date),
                "attempts": attempts,
                "landed": landed
            })

            save_data(st.session_state.tricks)
            st.success("Practice session saved!")
# ========================
# Dashboard
# ========================
elif page == "Dashboard":
    st.header("Skater Stats")

    if not st.session_state.tricks:
        st.title("🛹")
        st.info("No quests active. Add your first trick.")
    else:
        for trick_name, data in st.session_state.tricks.items():
            attempts = data["attempts"]
            landed = data["landed"]
            success_rate = (landed / attempts * 100) if attempts > 0 else 0


            st.subheader(trick_name)

            xp = landed * 10 + attempts
            level = xp // 100 + 1
            xp_progress = (xp % 100) / 100

            col1, col2, col3 = st.columns(3)

            col1.metric("Level", level)
            col2.metric("XP", xp)
            col3.metric("Mastery", f"{success_rate:.2f}%")
            
            st.progress(xp_progress)

            st.write(f"Difficulty: {data['difficulty']}")
            st.write(f"Goal: {data['goal']}")
            st.write(f"Attempts: {attempts}")
            st.write(f"Landed: {landed}")

            if data["youtube_links"]:
                st.write("Mentor Scrolls / Reference Videos:")
                for link in data["youtube_links"]:
                    st.video(link)

            if "history" in data and data["history"]:
                history_df = pd.DataFrame(data["history"])

                history_df["success_rate"] = history_df.apply(
                    lambda row: round((row["landed"] / row["attempts"]) * 100, 2)
                    if row["attempts"] > 0 else 0,
                    axis=1
                )

                st.write("Success Rate Over Time in (%)")
                st.line_chart(
                    history_df,
                    x="date",
                    y="success_rate"
                )

            if "history" in data and data["history"]:
                st.write("Practice History:")
                for session in data["history"]:
                    st.write(
                        f"- {session['date']}: "
                        f"{session['attempts']} attempts, "
                        f"{session['landed']} landed"
                    )
            if data["notes"]:
                st.write("Notes:")
                for note in data["notes"]:
                    st.write(f"- {note}")

            if st.button(f"Delete {trick_name}"):
                del st.session_state.tricks[trick_name]
                save_data(st.session_state.tricks)
                st.rerun()





            st.divider()



