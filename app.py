# Task 1: Simple welcome message
print("Welcome to the Study Time Tracker!")

# Task 2: Ask the user for their study hours today
hours_input = input("How many hours did you study today? ")

# Task 3: Convert input to a number and estimate weekly study hours
hours_today = float(hours_input)
estimated_weekly_hours = hours_today * 7

# Task 4: Display the result clearly
print(f"If you keep this pace, you'll study about {estimated_weekly_hours:.1f} hours this week.")
