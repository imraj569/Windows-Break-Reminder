import sys
import time
import os
import ctypes
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox

# Set actual work and break durations (in seconds)
WORK_DURATION = 25 * 60  # 25 minutes
BREAK_DURATION = 5 * 60 # 5 minutes
REMINDER_INTERVAL = 10 * 60  # 10 minutes after skip for actual use
POPUP_TIMEOUT = 2 * 60  # 2 minutes in milliseconds

# List of health tips and suggestions
health_tips = [
    "💧 Stay hydrated! Drink a glass of water during your break.",
    "👀 Rest your eyes! Look away from the screen for 20 seconds.",
    "🧘‍♂️ Stretch your body! Do some light stretching exercises.",
    "🚶‍♂️ Take a short walk around the office.",
    "☕ Grab a cup of tea or coffee and relax.",
    "💤 Close your eyes and take deep breaths to relax.",
    "🤸‍♂️ Do a quick exercise like jumping jacks or push-ups.",
    "🎧 Listen to your favorite song and refresh your mind."
]

def is_pc_locked():
    """Check if the PC is likely locked by checking if the screen saver is active."""
    user32 = ctypes.windll.user32
    screen_saver_active = ctypes.c_bool()
    user32.SystemParametersInfoW(114, 0, ctypes.byref(screen_saver_active), 0)
    return screen_saver_active.value

def show_reminder():
    if is_pc_locked():
        print("PC is locked, skipping reminder.")
        start_timer(WORK_DURATION)
        return

    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Time to Take a Break!")

    # Choose a random health tip
    tip = random.choice(health_tips)
    msg.setText(f"You've been working for a while. Would you like to take a break?\n\n{tip}")

    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.button(QMessageBox.Yes).setText("Take a break now 🛌")
    msg.button(QMessageBox.No).setText("Skip for now ⏳")

    # Set a timer to automatically close the popup after 2 minutes
    auto_close_timer = QTimer(msg)
    auto_close_timer.timeout.connect(lambda: msg.done(QMessageBox.No))
    auto_close_timer.start(POPUP_TIMEOUT)

    user_choice = msg.exec_()

    if user_choice == QMessageBox.Yes:
        take_break()
    else:
        skip_break()

def take_break():
    print("Taking a break for 5 minutes...")
    lock_pc()
    time.sleep(BREAK_DURATION)  # Wait for the break duration
    start_timer(WORK_DURATION)  # Start work timer again

def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def skip_break():
    print("Skipping break. You will be reminded again in 10 minutes.")
    start_timer(REMINDER_INTERVAL)

def start_timer(duration):
    time.sleep(duration)
    show_reminder()

if __name__ == "__main__":
    print("Starting work timer for 25 minutes...")
    start_timer(WORK_DURATION)