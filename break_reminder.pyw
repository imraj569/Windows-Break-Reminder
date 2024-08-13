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
        self.root.title("Break Reminder")

        # Convert cm to pixels
        width_cm = config['reminder_width']
        height_cm = config['reminder_height']
        width_px = int(37.7953 * width_cm)
        height_px = int(37.7953 * height_cm)

        # Set window size
        self.root.geometry(f"{width_px}x{height_px}")
        self.root.attributes('-topmost', True)  # Keep window on top

        # Timer Label with smaller font size
        self.time_label = tk.Label(self.root, font=('Helvetica', config['timer_size']), bg='white', fg='black')
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

    #notification system for remind and tips
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
            app_icon=r"D:\Github Projects\Windows-Break-Reminder\DataBase\icon.ico",  # Replace with your app icon if you have one
            timeout= 2* 60  # Notification will disappear after 10 seconds
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

def lock_pc():
    """
    Locks the PC using Windows API.
    """
    ctypes.windll.user32.LockWorkStation()

def main():
    config = {
        'sound_path': r"D:\Github Projects\Windows-Break-Reminder\DataBase\sound.mp3",
        'work_gif_path': r"D:\Github Projects\Windows-Break-Reminder\DataBase\work.gif",
        'break_gif_path': r"D:\Github Projects\Windows-Break-Reminder\DataBase\break.gif",
        'hello_gif_path': r"D:\Github Projects\Windows-Break-Reminder\DataBase\hello.gif",
        'work_time': 25 *60,  # 25 minutes
        'break_time': 10 * 60,  # 10 minutes
        'reminder_width': 5.5,  # reminder width in cm
        'reminder_height': 5.8,  # reminder height in cm
        'gif_width': 150,  # in pixels
        'gif_height': 150,  # in pixels
        'timer_size': 15,  # size of the timer
    }

    os.system('cls')  # Clear the screen
    app = TimerApp(config)
    app.root.mainloop()

if __name__ == "__main__":
    main()
