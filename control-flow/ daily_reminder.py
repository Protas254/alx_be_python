# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Enter the task's priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Modify reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Print the customized reminder
print(reminder)
