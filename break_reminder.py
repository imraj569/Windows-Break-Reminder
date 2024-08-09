import time
from win10toast import ToastNotifier
import random
from keyboard import press_and_release

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

def lock_screen():
    press_and_release("win+l")

def remind_and_break(break_interval,brak_time):
    # Wait for the first 25 minutes before the first reminder
   
    time.sleep(break_interval * 60)
    
    while True:
        try:
            # Reminder notification
            toaster.show_toast("Reminder 🕒", "Time to take a 5-minute break! 🌟", duration=10)
            
            # Lock the PC screen
            lock_screen()
            
            # Wait for 25 minutes
            time.sleep(break_interval * 60)
            
            # During the break, show a health tip and wait for 5 minutes
            tip = random.choice(tips)
            toaster.show_toast("Break Time ⏳", f"Take a break! Tip: {tip}", duration=10)
            time.sleep(brak_time * 60)  # 5 minutes break

        except TypeError as e:
            print(f"Error: {e}")
            # Handle or log the exception as needed

if __name__ == "__main__":
    #25 is the break_interval & 5 is break_time
    remind_and_break(int(25,5))