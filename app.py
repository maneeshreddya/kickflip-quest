import streamlit as st

st.set_page_config(page_title="Kickflip Quest", page_icon="🛹")

if "tricks" not in st.session_state:
    st.session_state.tricks = {}

st.title("🛹 Kickflip Quest")
st.write("Track skate tricks, practice progress, notes, videos, and reference links.")

page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Add Trick", "Practice Log", "Dashboard"]
)

if page == "Home":
    st.header("Welcome")
    st.write("Use this app to track your skateboarding progress over time.")

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
                "youtube_links": []
            }
            st.success(f"{name} saved!")
        else:
            st.warning("Please enter a trick name.")

elif page == "Practice Log":
    st.header("Practice Log")

    if not st.session_state.tricks:
        st.write("Add a trick first.")
    else:
        selected_trick = st.selectbox(
            "Choose trick",
            list(st.session_state.tricks.keys())
        )

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

            st.success("Practice session saved!")

elif page == "Dashboard":
    st.header("Progress Dashboard")

    if not st.session_state.tricks:
        st.write("No tricks added yet.")
    else:
        for trick_name, data in st.session_state.tricks.items():
            attempts = data["attempts"]
            landed = data["landed"]
            success_rate = (landed / attempts * 100) if attempts > 0 else 0

            st.subheader(trick_name)
            st.write(f"Difficulty: {data['difficulty']}")
            st.write(f"Goal: {data['goal']}")
            st.write(f"Attempts: {attempts}")
            st.write(f"Landed: {landed}")
            st.progress(success_rate / 100)
            st.write(f"Success Rate: {success_rate:.2f}%")

            if data["youtube_links"]:
                st.write("Reference links:")
                for link in data["youtube_links"]:
                    st.write(link)

            if data["notes"]:
                st.write("Notes:")
                for note in data["notes"]:
                    st.write(f"- {note}")

            st.divider()

