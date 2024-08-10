---

# ⏰ Break Reminder Script with Screen Lock, Auto-Close Popups, and Health Tips

This Python script is designed to help you maintain a healthy work routine by reminding you to take regular breaks. The script locks your PC screen for a 5-minute break and tracks whether the break was successful (i.e., the PC was locked for the entire 5 minutes). If the break is skipped, the script will remind you every 10 minutes until a successful break is taken.

## 🚀 Features

- **Regular Break Reminders**: Receive notifications every 25 minutes to take a 5-minute break.
- **PC Screen Lock**: Automatically locks your screen to ensure you take the break.
- **Auto-Close Popups**: Reminder popups automatically close after 2 minutes if no action is taken.
- **Health Tips**: Displays a random health tip during each break to promote well-being.
- **Successful Break Detection**: The script checks if your PC remains locked for the full 5-minute break. If the break is successful, the next reminder will be after 25 minutes.
- **Flexible Reminder Cycle**: If a break is skipped, the script will remind you every 10 minutes until a successful break is detected.

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/imraj569/break-reminder-script.git
   ```

2. **Install the required packages**:

   ```bash
   pip install pyqt5
   ```

## 🛠️ Usage

Run the script from the command line or your favorite Python IDE:

```bash
python break_reminder.py
```

### Parameters:
- **Work Duration**: Time in minutes between successful breaks (default: 25 minutes).
- **Break Time**: Duration of each break in minutes (default: 5 minutes).
- **Reminder Interval**: Time in minutes before a new reminder is sent if the break is skipped (default: 10 minutes).
- **Popup Timeout**: Time in seconds before the reminder popup automatically closes (default: 2 minutes).

The script will start by waiting for 25 minutes before reminding you to take a break. If the break is successful, it will wait another 25 minutes before the next reminder. If the break is skipped, it will remind you every 10 minutes until you take a successful break.

## 🤖 Future Plans

In the future, this script will be integrated with AI to provide smarter notifications, personalized health tips, and enhanced user interaction.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---