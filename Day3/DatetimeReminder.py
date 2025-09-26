"""
3) Datetime Reminder Script
   - Ask user for a date (YYYY-MM-DD).
   - Calculate how many days remain until that date.
   - If it is in the past, print "This date has already passed."
   - Otherwise, save the reminder into "reminders.txt" in format:
        "{date} -> {days_left} days left"
   - Append multiple reminders without overwriting.
"""

from datetime import datetime

def validate_date(user_input:str):
    try:
        return datetime.strptime(user_input.strip(), "%Y-%m-%d")
    except ValueError:
        return None

def datetime_reminder():
    while True:
        user_input=input("Enter a date (YYYY-MM-DD):")
        reminder_date=validate_date(user_input)
        if reminder_date is None:
            print("Invalid format! Please enter in YYYY-MM-DD format.")
        else:
            break
    today=datetime.today()
    days_left=(reminder_date-today).days
    
    if days_left < 0:
        print("This date has already passed.")
    else:
        reminder_text = f"{reminder_date.date()} -> {days_left} days left"
        reminder_file="reminders.txt"
        with open(reminder_file,"a") as f:
            f.write(reminder_text+"\n")
        print(f"Reminder saved into {reminder_file}")
        print("Remidner:",reminder_text)
