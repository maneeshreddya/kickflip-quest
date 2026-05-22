# 🛹 Kickflip Quest

Kickflip Quest is a Streamlit-based skateboarding progress tracker and practice journal.  
It helps users track skate tricks, log practice attempts, record successful landings, write notes, save YouTube reference links, and view progress over time.

## Project Purpose

Many habit trackers only track whether something was completed or not. Kickflip Quest is different because it focuses on **skill improvement** rather than simple task completion.

The app is designed for beginner and intermediate skateboarders who want to monitor their progress while learning tricks.

## Features

- Add skateboarding tricks with difficulty and personal goals
- Log practice sessions with date, attempts, and successful landings
- Write practice notes after each session
- Save YouTube reference links for learning
- Track total attempts and landed tricks
- View success rate / mastery percentage
- XP and level system for motivation
- Progress chart using practice history
- Persistent data storage using a JSON file

## Advanced Concepts Used

This project demonstrates several Python programming concepts:

- File handling using JSON for saving and loading data
- Dictionaries and lists for storing trick and practice session data
- Functions for loading and saving program data
- Conditional logic for validating user actions
- Loops for displaying saved tricks, notes, links, and history
- External libraries:
  - Streamlit for the user interface
  - Pandas for organizing practice history data

## How to Run the Program

1. Make sure Python is installed.

2. Install required libraries:

```bash
pip install streamlit pandas
```

3. Run the program:

```bash
streamlit run app.py
```

---

## Files Included

- `app.py` → Main Streamlit application
- `.gitignore` → Files ignored by Git
- `data.json` → Local storage for trick progress

---

## Notes

The app uses `data.json` to store user progress locally.

If the file does not exist, the app starts with empty data.

Uploaded videos are currently previewed during runtime and may be permanently saved in future versions.

---

## Target Audience

Kickflip Quest is designed for skateboarders who want a simple and motivating way to track trick progress over time.

The application combines practice logging with game-inspired progression systems including XP, levels, and mastery percentage.

---

## Future Improvements

- Retro RPG-style visual theme
- Permanent video storage
- Goal completion tracker
- More detailed practice insights
- Export progress summaries