import tkinter as tk
import os
import ctypes
import pygame
from PIL import Image, ImageTk, ImageSequence
from plyer import notification
import random

pygame.mixer.init()  # Initialize pygame for sound playback

class TimerApp:
    def __init__(self, config):
        self.config = config

        self.root = tk.Tk()
        self.root.title("Reminder")

        # Convert cm to pixels
        width_cm = config['reminder_width']
        height_cm = config['reminder_height']
        width_px = int(37.7953 * width_cm)
        height_px = int(37.7953 * height_cm)

        # Set window size
        self.root.geometry(f"{width_px}x{height_px}")
        self.root.attributes('-topmost', True)  # Keep window on top

        # Timer Label with smaller font size
        self.time_label = tk.Label(self.root, font=('Helvetica', config['timer_size']))
        self.time_label.pack(pady=1)

        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=1)

        # Buttons with smaller font size
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer, font=('Helvetica', 8))
        self.start_button.pack(side=tk.LEFT, padx=1)

        self.take_break_button = tk.Button(self.button_frame, text="Take Break", command=self.take_break, state=tk.DISABLED, font=('Helvetica', 8))
        self.take_break_button.pack(side=tk.LEFT, padx=1)

        self.skip_break_button = tk.Button(self.button_frame, text="Skip Break", command=self.skip_break, state=tk.DISABLED, font=('Helvetica', 8))
        self.skip_break_button.pack(side=tk.LEFT, padx=1)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer, font=('Helvetica', 8))
        self.reset_button.pack(side=tk.LEFT, padx=1)

        self.dark_mode_button = tk.Button(self.button_frame, text="Dark Mode", command=self.toggle_dark_mode, font=('Helvetica', 8))
        self.dark_mode_button.pack(side=tk.LEFT, padx=1)

        # Timer settings
        self.work_time = config['work_time']
        self.break_time = config['break_time']
        self.remaining_time = self.work_time
        self.timer_running = False
        self.timer_id = None  # To keep track of the current timer

        # Load GIF images and handle frames correctly
        self.work_gif_frames = self.load_gif_frames(config['work_gif_path'])
        self.break_gif_frames = self.load_gif_frames(config['break_gif_path'])
        self.hello_gif_frames = self.load_gif_frames(config['hello_gif_path'])

        self.current_gif_frames = self.hello_gif_frames  # Start with the hello GIF
        self.gif_index = 0
        self.gif_label = tk.Label(self.root, image=self.hello_gif_frames[0])  # Initial image
        self.gif_label.pack(side=tk.TOP)  # Place at the top
        self.animate_gif()

        self.update_timer_display()

        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        x = (screenwidth - width) // 2
        y = (screenheight - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Initialize dark mode setting and apply theme
        self.dark_mode = config.get('dark_mode', False)
        self.apply_theme()

    def load_gif_frames(self, gif_path):
        frames = []
        try:
            gif = Image.open(gif_path)
            for frame in ImageSequence.Iterator(gif):
                frame = frame.resize((self.config['gif_width'], self.config['gif_height']))  # Resize the frame to configured size
                frames.append(ImageTk.PhotoImage(frame))
        except Exception as e:
            print(f"Error loading GIF frames: {e}")
        return frames

    def update_timer_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        timer_text = '{:02d}:{:02d}'.format(int(minutes), int(seconds))
        self.time_label.config(text=timer_text)

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state=tk.DISABLED)
        self.take_break_button.config(state=tk.NORMAL)
        self.skip_break_button.config(state=tk.NORMAL)
        self.run_timer()
        self.switch_to_work_gif()  # Start the work GIF when the timer starts

    # notification system for remind and tips
    def notify_break(self):
        messages = [
            "Take a short break! 🚶‍♀️🚶‍♂️ Fresh air and movement boost energy.",
            "Stretch your body! 🤸‍♀️🤸‍♂️ Improves flexibility and reduces stress.",
            "Drink some water! 💧💧 Hydration is key for focus and well-being.",
            "Practice deep breathing! 🧘‍♂️🧘‍♀️ Calms your mind and reduces anxiety.",
            "Get some sunlight! ☀️☀️ Vitamin D is essential for good health.",
            "Eat a healthy snack! 🍎🍏 Nourish your body for optimal performance.",
        ]
        message = random.choice(messages)
        notification.notify(
            title="Time for a Break! Boss",
            message=message,
            app_icon=self.config['notification_icon'],  # Use the icon from config
            timeout=self.config['notification_timeout']  # Use the timeout from config
        )

    def run_timer(self):
        if not self.timer_running:
            return

        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
            self.timer_id = self.root.after(1000, self.run_timer)  # Schedule next update in 1 second
        else:
            self.timer_running = False
            self.play_sound()  # Play sound when timer reaches 0
            self.time_label.config(text="Time to take a break!")
            self.notify_break()
            self.take_break_button.config(state=tk.NORMAL)
            self.skip_break_button.config(state=tk.NORMAL)
            self.switch_to_break_gif()  # Switch to the break GIF

    def play_sound(self):
        try:
            # Load the sound using pygame
            pygame.mixer.music.load(self.config['sound_path'])
            pygame.mixer.music.play(-1)  # Play in a loop
        except pygame.error as e:
            print(f"Error playing sound: {e}")

    def take_break(self):
        self.stop_sound()  # Stop any playing sound
        self.stop_gif_animation()  # Stop the current GIF
        lock_pc()
        self.timer_running = False  # Stop the timer
        self.remaining_time = self.work_time  # Reset to work time after break
        self.update_timer_display()
        self.start_button.config(state=tk.NORMAL)  # Re-enable the Start button
        self.take_break_button.config(state=tk.DISABLED)
        self.skip_break_button.config(state=tk.DISABLED)
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel any running timer
        self.switch_to_hello_gif()  # Switch to the hello GIF during break

    def stop_sound(self):
        pygame.mixer.music.stop()

    def skip_break(self):
        self.stop_sound()  # Stop any playing sound
        self.stop_gif_animation()  # Stop the current GIF
        self.timer_running = False  # Stop the current timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel the existing timer
        self.remaining_time = self.break_time  # Set to break time
        self.update_timer_display()
        self.start_timer()  # Start the timer for break
        self.switch_to_work_gif()  # Switch to the work GIF

    def reset_timer(self):
        self.stop_sound()  # Stop any playing sound
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel any running timer
        self.remaining_time = self.work_time
        self.update_timer_display()
        self.start_button.config(state=tk.NORMAL)
        self.take_break_button.config(state=tk.DISABLED)
        self.skip_break_button.config(state=tk.DISABLED)
        self.switch_to_hello_gif()  # Ensure the hello GIF is displayed during wait time

    def animate_gif(self):
        self.gif_label.config(image=self.current_gif_frames[self.gif_index])
        self.gif_index = (self.gif_index + 1) % len(self.current_gif_frames)
        self.gif_label.after(150, self.animate_gif)  # Adjusted delay for slower animation

    def stop_gif_animation(self):
        self.gif_label.after_cancel(self.gif_label)  # Stop the current GIF animation

    def switch_to_work_gif(self):
        self.stop_gif_animation()  # Stop the current GIF animation
        self.current_gif_frames = self.work_gif_frames
        self.gif_index = 0
        self.animate_gif()  # Start the work GIF animation

    def switch_to_break_gif(self):
        self.stop_gif_animation()  # Stop the current GIF animation
        self.current_gif_frames = self.break_gif_frames
        self.gif_index = 0
        self.animate_gif()  # Start the break GIF animation

    def switch_to_hello_gif(self):
        self.stop_gif_animation()  # Stop the current GIF animation
        self.current_gif_frames = self.hello_gif_frames
        self.gif_index = 0
        self.animate_gif()  # Start the hello GIF animation

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            # Dark mode settings
            self.root.config(bg='black')
            self.time_label.config(bg='black', fg='white')
            self.start_button.config(bg='gray20', fg='white')
            self.take_break_button.config(bg='gray20', fg='white')
            self.skip_break_button.config(bg='gray20', fg='white')
            self.reset_button.config(bg='gray20', fg='white')
            self.dark_mode_button.config(bg='gray20', fg='white')

            # Update the button text to indicate light mode
            self.dark_mode_button.config(text="Light Mode")
        else:
            # Light mode settings
            self.root.config(bg='white')
            self.time_label.config(bg='white', fg='black')
            self.start_button.config(bg='SystemButtonFace', fg='black')
            self.take_break_button.config(bg='SystemButtonFace', fg='black')
            self.skip_break_button.config(bg='SystemButtonFace', fg='black')
            self.reset_button.config(bg='SystemButtonFace', fg='black')
            self.dark_mode_button.config(bg='SystemButtonFace', fg='black')

            # Update the button text to indicate dark mode
            self.dark_mode_button.config(text="Dark Mode")

    def run(self):
        self.root.mainloop()

def lock_pc():
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception as e:
        print(f"Error locking the workstation: {e}")

# Configuration settings for the timer and notifications
config = {
    'work_time':  25*60,  # Work time in seconds (45 minutes)
    'break_time': 10*60,  # Break time in seconds (10 minutes)
    'timer_size': 12,  # Smaller font size for timer display
    'reminder_width': 7,  # Window width in centimeters
    'reminder_height': 5,  # Window height in centimeters
    'work_gif_path': r'D:\Github Projects\Windows-Break-Reminder\DataBase\work.gif',  # Path to the GIF to display during work
    'break_gif_path': r'D:\Github Projects\Windows-Break-Reminder\DataBase\break.gif',  # Path to the GIF to display during break
    'hello_gif_path': r'D:\Github Projects\Windows-Break-Reminder\DataBase\hello.gif',  # Path to the GIF to display initially or during wait
    'gif_width': 100,  # Width of the GIF in pixels
    'gif_height': 100,  # Height of the GIF in pixels
    'sound_path': r'D:\Github Projects\Windows-Break-Reminder\DataBase\sound.mp3',  # Path to the sound file to play when the timer reaches 0
    'notification_icon': r'D:\Github Projects\Windows-Break-Reminder\DataBase\icon.ico',  # Path to the notification icon
    'notification_timeout': 2*60,  # Timeout for notifications in seconds
    'dark_mode': False,  # Default mode (False for light mode, True for dark mode)
}

if __name__ == "__main__":
    app = TimerApp(config)
    app.run()
