import streamlit as st

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

# Initialize session state to store tasks and schedules
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if 'work_schedule' not in st.session_state:
    st.session_state.work_schedule = {
        "Weekdays": {"Work Time": "", "Quiet Time": ""},
        "Weekends": {"Work Time": "", "Quiet Time": ""},
    }

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