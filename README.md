---

# Windows Break Reminder 🕒

Welcome to **Windows Break Reminder**, your ultimate tool for maintaining productivity and wellness during long computer sessions! This application helps you stay on track with regular breaks, provides visual and auditory reminders, and even locks your PC to ensure you take those necessary breaks.

## 🚀 Features

- **⏲️ Start Timer**: Begin the countdown for your work session with ease.
- **🚪 Take Break**: Lock your PC and reset the timer for your next work session.
- **⏩ Skip Break**: Start a 30-second countdown before reminding you to take a break again.
- **🔄 Reset Timer**: Reset the timer to the initial work duration.
- **🎥 Animated GIFs**: Enjoy visual feedback with animated GIFs during work, break, and idle times.
- **🌙 Dark Mode**: Toggle between Dark Mode and Light Mode to suit your environment.

## 🌟 Latest Release

[![Latest Release](https://img.shields.io/github/v/release/imraj569/Windows-Break-Reminder?label=Latest%20Release)](https://github.com/imraj569/Windows-Break-Reminder/releases/latest)
### v0.0.2 (August 2024) 🚀

- **Enhanced Dark Mode**: Toggle between Dark Mode and Light Mode with updated visual elements and text. 🌙💡
- **New Reminder Messages**: Added variety to notification messages for breaks with helpful tips. 💬
- **Improved GIF Animation**: Smoother and more engaging GIF animations during different timer states. 🎞️

## 📦 Installation

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

## ⚙️ Configuration

Customize the application by modifying the `config` dictionary in the `main()` function of the script:

- **`work_time`**: Duration of the work session in seconds (default is 25 minutes).
- **`break_time`**: Duration of the break period in seconds (default is 30 seconds).
- **`sound_path`**: Path to the sound file used for notifications.
- **`work_gif_path`**: Path to the GIF displayed during work sessions.
- **`break_gif_path`**: Path to the GIF displayed during breaks.
- **`hello_gif_path`**: Path to the GIF displayed during idle times.
- **`reminder_width`**: Width of the reminder window in cm.
- **`reminder_height`**: Height of the reminder window in cm.
- **`gif_width`**: Width of GIFs in pixels.
- **`gif_height`**: Height of GIFs in pixels.
- **`timer_size`**: Font size of the timer display.

## 🤝 Contributing

Feel free to fork the repository and submit a pull request if you have suggestions or improvements!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Rajkishor Patra** - [GitHub Profile](https://github.com/imraj569/)

---