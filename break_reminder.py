import tkinter as tk
import os
import ctypes

class TimerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Break Reminder")
        
        # Convert cm to pixels (approximately 37.7953 pixels per cm)
        width_cm = 7
        height_cm = 2
        width_px = int(37.7953 * width_cm)
        height_px = int(37.7953 * height_cm)
        
        # Set window size
        self.root.geometry(f"{width_px}x{height_px}")
        self.root.attributes('-topmost', True)  # Keep window on top

        # Timer Label with smaller font size
        self.time_label = tk.Label(self.root, font=('Helvetica', 12), bg='white', fg='black')
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
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 10 * 60  # 10 minutes
        self.remaining_time = self.work_time
        self.timer_running = False
        self.timer_id = None  # To keep track of the current timer

        self.update_timer_display()

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

    def run_timer(self):
        if not self.timer_running:
            return

        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
            self.timer_id = self.root.after(1000, self.run_timer)  # Schedule next update in 1 second
        else:
            self.timer_running = False
            self.time_label.config(text="Time to take a break!🍵")
            self.take_break_button.config(state=tk.NORMAL)
            self.skip_break_button.config(state=tk.NORMAL)

    def take_break(self):
        lock_pc()
        self.timer_running = False  # Stop the timer
        self.remaining_time = self.work_time  # Reset to work time after break
        self.update_timer_display()
        self.start_button.config(state=tk.NORMAL)  # Re-enable the Start button
        self.take_break_button.config(state=tk.DISABLED)
        self.skip_break_button.config(state=tk.DISABLED)
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel any running timer

    def skip_break(self):
        self.timer_running = False  # Stop the current timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel the existing timer
        self.remaining_time = self.break_time  # Set to skip break time
        self.update_timer_display()
        self.start_timer()  # Start the skip break timer

    def reset_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)  # Cancel any running timer
        self.remaining_time = self.work_time
        self.update_timer_display()
        self.start_button.config(state=tk.NORMAL)
        self.take_break_button.config(state=tk.DISABLED)
        self.skip_break_button.config(state=tk.DISABLED)

def lock_pc():
    """
    Locks the PC using Windows API.
    """
    ctypes.windll.user32.LockWorkStation()

def main():
    os.system('cls')  # Clear the screen
    app = TimerApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()
