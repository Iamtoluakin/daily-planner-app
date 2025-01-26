import streamlit as st
import random
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Custom CSS for deep blue theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0A1A2F;
        color: #FFFFFF;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1A2A4F;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #1A2A4F;
        color: #FFFFFF;
        border: 1px solid #2A3A6F;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #2A3A6F;
        border-color: #3A4A8F;
    }
    .stHeader {
        color: #FFFFFF;
    }
    .stSubheader {
        color: #FFFFFF;
    }
    .stMarkdown {
        color: #FFFFFF;
    }
    .stSuccess {
        color: #00FF00;
    }
    .stWarning {
        color: #FFA500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# List of New Testament verses taught by Jesus
bible_verses = [
    "Matthew 5:44 - But I tell you, love your enemies and pray for those who persecute you.",
    "Matthew 6:33 - But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
    "Matthew 7:7 - Ask and it will be given to you; seek and you will find; knock and the door will be opened to you.",
    "John 14:6 - Jesus answered, 'I am the way and the truth and the life. No one comes to the Father except through me.'",
    "John 8:12 - When Jesus spoke again to the people, he said, 'I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life.'",
    "Matthew 11:28 - Come to me, all you who are weary and burdened, and I will give you rest.",
    "Matthew 22:37-39 - Jesus replied: 'Love the Lord your God with all your heart and with all your soul and with all your mind. This is the first and greatest commandment. And the second is like it: Love your neighbor as yourself.'",
    "John 3:16 - For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
    "Matthew 5:16 - In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",
    "John 15:12 - My command is this: Love each other as I have loved you."
]

# Function to send an email with a random Bible verse
def send_email(verse, email):
    message = Mail(
        from_email="your-email@example.com",  # Replace with your verified SendGrid email
        to_emails=email,
        subject="Hourly Bible Verse",
        html_content=f"<strong>{verse}</strong>"
    )
    try:
        sg = SendGridAPIClient(st.secrets["SENDGRID_API_KEY"])
        response = sg.send(message)
        st.success(f"Email sent to {email}!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# Initialize session state to store tasks and schedules
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if 'work_schedule' not in st.session_state:
    st.session_state.work_schedule = {
        "Weekdays": {"Work Time": "", "Quiet Time": ""},
        "Weekends": {"Work Time": "", "Quiet Time": ""},
    }

if 'current_verse' not in st.session_state:
    st.session_state.current_verse = random.choice(bible_verses)

# App Title
st.title("📅 Daily Planner App")

# Section for adding tasks
st.header("➕ Add Tasks")
task = st.text_input("Enter a new task:")
priority = st.selectbox("Select priority:", ["Low", "Medium", "High"])

if st.button("Add Task"):
    if task:
        task_with_priority = f"{task} (Priority: {priority})"
        st.session_state.tasks.append(task_with_priority)
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task!")

# Section for displaying tasks
st.header("📋 Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {task}")
else:
    st.write("No tasks added yet.")

# Button to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")

# Section for work and quiet time scheduling
st.header("⏰ Work and Quiet Time Schedule")

# Input for work and quiet time for weekdays and weekends
st.subheader("📅 Weekdays (Monday to Friday)")
col1, col2 = st.columns(2)

with col1:
    work_time_weekdays = st.text_input(
        "Work Time (Weekdays):",
        value=st.session_state.work_schedule["Weekdays"]["Work Time"]
    )
    st.session_state.work_schedule["Weekdays"]["Work Time"] = work_time_weekdays

with col2:
    quiet_time_weekdays = st.text_input(
        "Quiet Time (Weekdays):",
        value=st.session_state.work_schedule["Weekdays"]["Quiet Time"]
    )
    st.session_state.work_schedule["Weekdays"]["Quiet Time"] = quiet_time_weekdays

st.subheader("🌅 Weekends (Saturday and Sunday)")
col3, col4 = st.columns(2)

with col3:
    work_time_weekends = st.text_input(
        "Work Time (Weekends):",
        value=st.session_state.work_schedule["Weekends"]["Work Time"]
    )
    st.session_state.work_schedule["Weekends"]["Work Time"] = work_time_weekends

with col4:
    quiet_time_weekends = st.text_input(
        "Quiet Time (Weekends):",
        value=st.session_state.work_schedule["Weekends"]["Quiet Time"]
    )
    st.session_state.work_schedule["Weekends"]["Quiet Time"] = quiet_time_weekends

# Display the schedule
st.header("📅 Your Weekly Schedule")
st.write("**📅 Weekdays (Monday to Friday)**")
st.write(f"- Work Time: {st.session_state.work_schedule['Weekdays']['Work Time']}")
st.write(f"- Quiet Time: {st.session_state.work_schedule['Weekdays']['Quiet Time']}")
st.write("---")
st.write("**🌅 Weekends (Saturday and Sunday)**")
st.write(f"- Work Time: {st.session_state.work_schedule['Weekends']['Work Time']}")
st.write(f"- Quiet Time: {st.session_state.work_schedule['Weekends']['Quiet Time']}")

# Section for random Bible verses
st.header("📖 Random Bible Verse")
st.write("Here’s a verse taught by Jesus to inspire you:")
st.write(f"**{st.session_state.current_verse}**")

if st.button("Show Another Verse"):
    st.session_state.current_verse = random.choice(bible_verses)

# Section for email notifications
st.header("🔔 Hourly Bible Verse Notifications")
email = st.text_input("Enter your email to receive hourly Bible verses:")

if st.button("Subscribe for Notifications"):
    if email:
        # Send the first verse immediately
        send_email(st.session_state.current_verse, email)
        # Schedule hourly notifications (this is a placeholder; see notes below)
        st.write("You will receive hourly Bible verses starting now!")
    else:
        st.warning("Please enter a valid email address.")