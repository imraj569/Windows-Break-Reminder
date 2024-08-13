---

# Break Reminder 🕒

Welcome to the **Break Reminder** application! This tool helps you take regular breaks while working on your computer by using a countdown timer, providing options to take or skip breaks, and even locking your PC when a break is taken. This new version includes several improvements and new features.

## New Features 🚀

- **Dark Mode**: Toggle between dark and light modes for a better visual experience.
- **Animated GIFs**: Updated animations for work, break, and idle times.
- **Enhanced Notifications**: Includes motivational tips and reminders with customizable icons and timeout settings.
- **Smaller Font Size**: Improved readability with a smaller font size for timer display.
- **Reset Timer Button**: Added functionality to reset the timer to the initial work duration.

## Features 🛠️

- **Start Timer**: Begin the countdown for your work session.
- **Take Break**: Lock your PC and reset the timer for your next work session.
- **Skip Break**: Start a countdown before reminding you to take a break again.
- **Reset Timer**: Reset the timer to the initial work duration.
- **Animated GIFs**: Visual feedback with updated animated GIFs during work, break, and idle times.

## How to Use 💡

1. **Start Timer**: Click the "Start" button to begin the countdown. The work GIF will start animating.
2. **Take Break**: Click "Take Break" when you’re ready for a break. Your PC will lock, the timer will reset, and the hello GIF will display during the break.
3. **Skip Break**: If you want to skip the break, click "Skip Break." The timer will be set to the break time, and the work GIF will animate.
4. **Reset Timer**: Use the "Reset" button to reset the timer to the default work duration and display the hello GIF.

## Installation 💻

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/imraj569/Windows-Break-Reminder.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd Windows-Break-Reminder
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:

   Double-click `break_reminder.pyw` to run the application (it will run in the background without a console window).

## Requirements 📋

- **Python 3.x**: Ensure you have Python installed on your system.
- **Windows OS**: The script uses Windows-specific functionality to lock the PC.
- **Pillow**: For handling GIF images.
- **pygame**: For sound playback.
- **plyer**: For system notifications.

## Configuring the Application ⚙️

You can customize various settings by modifying the `config` dictionary in the `main()` function of the script:

- **`work_time`**: Duration of the work session in seconds (default is 25 minutes).
- **`break_time`**: Duration of the break period in seconds (default is 10 minutes).
- **`sound_path`**: Path to the sound file used for notifications.
- **`work_gif_path`**: Path to the GIF displayed during work sessions.
- **`break_gif_path`**: Path to the GIF displayed during breaks.
- **`hello_gif_path`**: Path to the GIF displayed during idle times.
- **`reminder_width`**: Width of the reminder window in cm.
- **`reminder_height`**: Height of the reminder window in cm.
- **`gif_width`**: Width of GIFs in pixels.
- **`gif_height`**: Height of GIFs in pixels.
- **`timer_size`**: Font size of the timer display.
- **`notification_icon`**: Path to the notification icon.
- **`notification_timeout`**: Timeout for notifications in seconds.
- **`dark_mode`**: Set to `True` to enable dark mode or `False` for light mode.

## Contributing 🤝

Feel free to fork the repository and submit a pull request if you have suggestions or improvements!

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
