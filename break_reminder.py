import time
from win10toast import ToastNotifier
import random
from keyboard import press_and_release
import ctypes

# Create an instance of ToastNotifier
toaster = ToastNotifier()

# List of health tips or exercises with emojis
tips = [
    "👁️ Do some eye exercises: Look at an object 20 feet away for 20 seconds.",
    "🧘 Stand up and stretch your arms and legs for a few seconds.",
    "👀 Blink your eyes rapidly for 20 seconds to refresh them.",
    "🌬️ Take a deep breath and relax for a moment.",
    "🔄 Rotate your shoulders in a circular motion to release tension."
]

# Function to lock the screen
def lock_screen():
    press_and_release("win+l")

# Function to check if the screen is locked
def is_screen_locked():
    user32 = ctypes.windll.user32
    idle_time = user32.GetTickCount() - user32.GetLastInputInfo()
    return idle_time > 5000  # Screen locked if idle time > 5 seconds

# Function to check if the break is successful
def is_break_successful(break_time):
    start_time = time.time()
    while time.time() - start_time < break_time * 60:
        if not is_screen_locked():
            return False
        time.sleep(2)  # Check every 2 seconds
    return True

# Main function to handle reminders and breaks
def remind_and_break(break_interval, break_time):
    time.sleep(break_interval * 60)  # Skip first break, wait for 25 minutes
    
    while True:
        # Select a random tip
        tip = random.choice(tips)
        
        # Reminder notification
        toaster.show_toast("Reminder 🕒", f"Time to take a 5-minute break! 🌟 {tip}", duration=10)
        
        # Lock the PC screen
        lock_screen()
        
        # Check if the break is successful
        if is_break_successful(break_time):
            print("Break was successful.")
            time.sleep(break_interval * 60)  # Wait for 25 minutes before the next reminder
        else:
            print("Break was not successful. Reminding again in 10 minutes.")
            time.sleep(10 * 60)  # Remind again in 10 minutes if the break was not successful
            continue  # Skip the next interval wait and remind again immediately

if __name__ == "__main__":
    # 25 is the break_interval & 5 is break_time
    remind_and_break(25, 5)
