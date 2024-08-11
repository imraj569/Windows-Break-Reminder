
---

# Break Reminder 🕒

Welcome to the **Break Reminder** application! This simple tool is designed to help you take regular breaks while working on your computer. It uses a countdown timer and provides options to take or skip breaks, and even locks your PC when a break is taken.

## Features 🚀

- **Start Timer**: Begin the countdown for your work session.
- **Take Break**: Lock your PC and reset the timer for your next work session.
- **Skip Break**: Start a 10-minute countdown before reminding you to take a break again.
- **Reset Timer**: Reset the timer to the initial work duration.

## How to Use 🛠️

1. **Start Timer**: Click the "Start" button to begin the countdown.
2. **Take Break**: When you’re ready for a break, click "Take Break." Your PC will lock, and the timer will reset.
3. **Skip Break**: If you want to skip the break, click "Skip Break." The timer will be set to 10 minutes before reminding you again.
4. **Reset Timer**: Use the "Reset" button to reset the timer to the default work duration.

## Installation 💻

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/imraj569/Windows-Break-Reminder.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd Windows-Break-Reminder
   ```

3. **Install Requirements file**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:

   Double-click `break_reminder.pyw` to run the application (it will run in the background without a console window).

## Requirements 📋

- **Python 3.x**: Ensure you have Python installed on your system.
- **Windows OS**: The script uses Windows-specific functionality to lock the PC.

## Customizing Timer Durations 🕰️

You can customize the work and break durations by modifying the `self.work_time` and `self.break_time` variables in the script. The values are in seconds:

- **Work Time**: Default is 25 minutes (1500 seconds).
- **Break Time**: Default is 10 minutes (600 seconds).

## Contributing 🤝

Feel free to fork the repository and submit a pull request if you have suggestions or improvements!

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
