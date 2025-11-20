"""
Study Time Tracker
------------------
A simple Python program that asks for today's study hours,
estimates your weekly study time, and shows your progress
toward a weekly study goal.
"""

# --- Task 1: Welcome message ---
print("Welcome to the Study Time Tracker!")

# --- Task 2: Ask the user for input ---
hours_input = input("How many hours did you study today? ")

# --- Tasks 3 & 5: Convert input and handle errors ---
try:
    # Try to convert the input to a floating-point number
    hours_today = float(hours_input)

    # Check for negative study time
    if hours_today < 0:
        print("Please enter a non-negative number of hours.")
        exit()

except ValueError:
    # Runs if conversion to float fails
    print("Please enter a valid number for hours (for example: 2 or 2.5).")
    exit()

# --- Task 3: Perform calculation ---
# Estimate weekly study hours by multiplying today's hours by 7
estimated_weekly_hours = hours_today * 7

# Set a weekly study goal in hours
weekly_goal = 14

# Calculate progress toward the goal as a percentage
progress_percent = (estimated_weekly_hours / weekly_goal) * 100

# --- Task 4: Display results clearly ---
print()  # blank line for readability
print(f"If you keep this pace, you'll study about {estimated_weekly_hours:.1f} hours this week.")
print(f"Your weekly study goal is {weekly_goal} hours.")
print(f"That means you are at {progress_percent:.1f}% of your weekly goal.")

# Give a simple message based on their progress
if progress_percent < 50:
    print("You're getting started—try to add a bit more study time!")
elif progress_percent < 100:
    print("Nice work! You're on your way to meeting your goal.")
else:
    print("Great job! You're on track to meet or exceed your goal this week.")

# --- Task 6: Code is commented, cleaned, and ready ---
