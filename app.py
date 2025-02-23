import streamlit as st
import random
import json
import os

# Function to load data
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

# Function to save data
def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

# Title and Branding
st.title("🌟 Growth Mindset Challenge 🎯")
st.markdown("<h1 style='color: green;'>🍒🌟 Created By Arjumand Afreen Tabinda🎯</h1>", unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio("📌 Navigate", [
    "🏠 Home", "📊 Progress Log", "📝 Reflection", "🎯 Goals", "🔥 Daily Challenge", 
    "💬 Motivation", "📚 Learning Resources", "🏆 Success Stories", "📅 Habit Tracker", 
    "🧘 Mindfulness", "📝 Journaling Prompts", "🤝 Community Support", "🎖 Achievements Board"
])

# Home Page
def home():
    st.header("Welcome to Your Growth Journey!")

    # Expandable About Section
    with st.expander("📌 About Growth Mindset"):
        st.write("A growth mindset helps you learn and improve every day! Embrace challenges and keep growing. 🌱")
        st.image("https://source.unsplash.com/800x400/?success,motivation")
        st.write("### Why Growth Mindset Matters")
        st.write("- **Encourages lifelong learning**: You keep evolving.\n- **Helps overcome obstacles**: Embrace challenges as opportunities.\n- **Increases resilience and adaptability**: Bounce back from failures and grow stronger.")

    # Interactive Section: Set Your First Goal
    st.subheader("🎯 Start Your Journey: Set Your First Goal Today!")
    goal = st.text_input("What is your goal for today?")
    if st.button("Save Goal"):
        if goal.strip():
            goals = load_data("goals.json")
            goals.append({"goal": goal})
            save_data("goals.json", goals)
            st.success(f"Goal saved: {goal}")
        else:
            st.warning("Please enter a goal to proceed.")

    # Interactive Section: Reflect on Your Day
    st.subheader("📝 Reflect on Your Day")
    reflection = st.text_area("What did you learn today or what challenge did you face?")
    if st.button("Save Reflection"):
        if reflection.strip():
            reflections = load_data("reflections.json")
            reflections.append({"text": reflection})
            save_data("reflections.json", reflections)
            st.success(f"Reflection saved: {reflection}")
        else:
            st.warning("Please write your reflection.")

    # Daily Challenge Preview
    st.subheader("🔥 Today's Growth Challenge")
    challenges = [
        "Learn something new today!",
        "Reflect on a mistake and what you learned.",
        "Ask for feedback and apply it.",
        "Set a mini goal and achieve it.",
        "Celebrate effort, not just results.",
        "Step outside your comfort zone.",
        "Practice gratitude for today's learning.",
        "Turn a failure into a learning experience."
    ]
    challenge = random.choice(challenges)
    st.write(f"**Today's Challenge:** {challenge}")
    st.image("https://source.unsplash.com/800x400/?challenge,goal")

    # Motivational Quote
    st.subheader("💬 Motivation for Today")
    quotes = [
        "Believe you can and you're halfway there.",
        "Your only limit is your mind.",
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Every day is a fresh start.",
        "Doubt kills more dreams than failure ever will.",
        "The best way to predict the future is to create it."
    ]
    st.write(f"**Quote of the Day:** {random.choice(quotes)}")
    st.image("https://source.unsplash.com/800x400/?motivation,success")

    # Include Extra Encouragement for Users
    st.subheader("🌱 Keep Going!")
    st.write("Remember, growth comes from embracing challenges and learning from both successes and failures. Keep pushing forward!")
    st.image("https://source.unsplash.com/800x400/?inspiration,progress")

    # Goal Setting and Reflection reminders
    st.subheader("💡 Keep Track of Your Growth")
    st.write("Don’t forget to regularly track your progress, set new goals, and reflect on your journey. It will help you stay motivated and see the improvements over time!")
    st.write("📈 **Tip**: Regular reflection can show you how far you’ve come, and goal setting helps you stay focused on what's important.")

# Progress Log Page
def progress_log():
    st.header("📊 Progress Log")
    with st.expander("📝 Track Progress"):
        progress = load_data("progress.json")
        entry = st.text_area("Log today's progress:")
        if st.button("Save Entry"):
            if entry.strip():
                progress.append({"entry": entry})
                save_data("progress.json", progress)
                st.success("Progress saved!")
    with st.expander("📜 Your Progress Logs"):
        if progress:
            for p in progress:
                st.write(f"- {p['entry']}")

# Reflection Page
def reflection():
    st.header("📝 Thought Reflection")
    with st.expander("✍️ Reflect on Your Day"):
        reflections = load_data("reflections.json")
        reflection = st.text_area("Write your thoughts for today:")
        if st.button("Save Reflection"):
            if reflection.strip():
                reflections.append({"text": reflection})
                save_data("reflections.json", reflections)
                st.success("Reflection saved!")
    with st.expander("📖 Past Reflections"):
        if reflections:
            for ref in reflections:
                st.write(f"- {ref['text']}")

# Goal Setting Page
def goal_setting():
    st.header("🎯 Set Your Goals")
    with st.expander("🎯 Define Your Goals"):
        goals = load_data("goals.json")
        goal = st.text_input("Your Goal:")
        if st.button("Save Goal"):
            if goal.strip():
                goals.append({"goal": goal})
                save_data("goals.json", goals)
                st.success("Goal saved!")
    with st.expander("📌 Your Goals"):
        if goals:
            for g in goals:
                st.write(f"- {g['goal']}")

# Daily Challenge Page
def daily_challenge():
    st.header("🔥 Daily Growth Challenge")
    with st.expander("💡 Today's Challenge"):
        challenges = [
            "Learn something new today!",
            "Reflect on a mistake and what you learned.",
            "Ask for feedback and apply it.",
            "Set a mini goal and achieve it.",
            "Celebrate effort, not just results.",
            "Step outside your comfort zone.",
            "Practice gratitude for today's learning.",
            "Turn a failure into a learning experience."
        ]
        challenge = random.choice(challenges)
        st.write(f"**Today's Challenge:** {challenge}")
        st.image("https://source.unsplash.com/800x400/?challenge,goal")

# Motivational Quotes Page
def motivation():
    st.header("💬 Motivational Quotes")
    with st.expander("🌟 Inspiration"):
        quotes = [
            "Believe you can and you're halfway there.",
            "Your only limit is your mind.",
            "Dream big, work hard, stay focused, and surround yourself with good people.",
            "Every day is a fresh start.",
            "Doubt kills more dreams than failure ever will.",
            "The best way to predict the future is to create it."
        ]
        st.write(f"**Quote of the day:** {random.choice(quotes)}")
        st.image("https://source.unsplash.com/800x400/?motivation,success")

# Learning Resources Page
def learning_resources():
    st.header("📚 Learning Resources")
    resources = [
        {"title": "Growth Mindset Guide", "link": "https://www.mindsetworks.com/science/"},
        {"title": "How to Build Good Habits", "link": "https://jamesclear.com/atomic-habits"},
        {"title": "Resilience and Overcoming Challenges", "link": "https://www.psychologytoday.com/us/basics/resilience" }
    ]
    for resource in resources:
        st.markdown(f"📖 [{resource['title']}]({resource['link']})")

# Other pages like Success Stories, Habit Tracker, etc. can remain as is
# Just copy the other functions (progress_log, reflection, etc.) as needed from your original code
# Success Stories Page
def success_stories():
    st.header("🏆 Success Stories")
    with st.expander("📢 Share Your Story"):
        stories = load_data("success_stories.json")
        story = st.text_area("Write about a success you've achieved:", key="success_story_input")
        if st.button("Share Story"):
            if story.strip():
                stories.append({"story": story})
                save_data("success_stories.json", stories)
                st.success("🎉 Congratulations! Your success story is inspiring!")
            else:
                st.warning("Please enter a story.")
    with st.expander("🌟 Community Success Stories"):
        if stories:
            for s in stories:
                st.write(f"- {s['story']}")

 
## ... previous code remains the same ...
# Habit Tracker Page
def habit_tracker():
    st.header("📅 Habit Tracker")
    with st.expander("✔️ Track Your Habits"):
        habits = load_data("habits.json")
        habit = st.text_input("Enter a habit to track:")
        if st.button("Add Habit"):
            if habit.strip():
                habits.append({"habit": habit})
                save_data("habits.json", habits)
                st.success("✅ Habit added! Keep going!")
    with st.expander("📌 Your Tracked Habits"):
        if habits:
            for h in habits:
                st.write(f"- {h['habit']}")

# Mindfulness Page
def mindfulness():
    st.header("🧘 Mindfulness")
    with st.expander("🌿 Mindfulness Exercises"):
        mindfulness_tips = [
            "Take 5 deep breaths and focus on your inhale and exhale.",
            "Spend 5 minutes in complete silence, observing your surroundings.",
            "Do a quick body scan meditation.",
            "Write down 3 things you're grateful for today."
        ]
        st.write(f"**Try this:** {random.choice(mindfulness_tips)}")

# Journaling Prompts Page
def journaling_prompts():
    st.header("📝 Journaling Prompts")
    with st.expander("✍️ Writing Inspiration"):
        prompts = [
            "What is one thing you learned today?",
            "Describe a challenge you faced and how you overcame it.",
            "Write about something that made you smile today.",
            "What are your top 3 priorities for the week?"
        ]
        st.write(f"**Try this prompt:** {random.choice(prompts)}")
        st.write("💡 *Tip:* Journaling daily can help you gain clarity and track progress.")

# Community Support Page
def community_support():
    st.header("🤝 Community Support")
    with st.expander("💬 Share Your Thoughts"):
        messages = load_data("community_support.json")
        message = st.text_area("Leave a message of support or ask for advice:")
        if st.button("Post Message"):
            if message.strip():
                messages.append({"message": message})
                save_data("community_support.json", messages)
                st.success("Your message has been posted!")
    with st.expander("📌 Community Messages"):
        if messages:
            for m in messages:
                st.write(f"- {m['message']}")

# Achievements Board Page
def achievements_board():
    st.header("🎖 Achievements Board")
    with st.expander("🏅 Record Your Achievements"):
        achievements = load_data("achievements.json")
        achievement = st.text_input("What did you accomplish today?")
        if st.button("Add Achievement"):
            if achievement.strip():
                achievements.append({"achievement": achievement})
                save_data("achievements.json", achievements)
                st.success("🎊 Great job! Keep achieving your goals!")
    with st.expander("🌟 Your Achievements"):
        if achievements:
            for a in achievements:
                st.write(f"- {a['achievement']}")




# Render the page based on the sidebar selection
if page == "🏠 Home":
    home()
elif page == "📊 Progress Log":
    progress_log()
elif page == "📝 Reflection":
    reflection()
elif page == "🎯 Goals":
    goal_setting()
elif page == "🔥 Daily Challenge":
    daily_challenge()
elif page == "💬 Motivation":
    motivation()
elif page == "📚 Learning Resources":
    learning_resources()
elif page == "🏆 Success Stories":
    success_stories()
elif page == "📅 Habit Tracker":
    habit_tracker()
elif page == "🧘 Mindfulness":
    mindfulness()
elif page == "📝 Journaling Prompts":
    journaling_prompts()
elif page == "🤝 Community Support":
    community_support()
elif page == "🎖 Achievements Board":
    achievements_board()  # Now this will work correctly
 