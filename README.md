```markdown
# Break Reminder

![Python](https://img.shields.io/badge/python-3.11-blue.svg)

## Overview

`break_reminder.pyw` is a simple Python-based script designed to help you take regular breaks while working. It reminds you to take a 5-minute break every 25 minutes, with an option to skip the break and be reminded again after 10 minutes. The script locks the PC when you decide to take a break and waits for you to manually start the timer again.

## Features

- **Pomodoro-style Timer**: The script operates on a 25-minute work cycle followed by a 5-minute break.
- **User Interaction**: When the break time is up, a popup window appears with three options:
  - **Start**: Starts the 25-minute countdown.
  - **Take Break**: Locks the PC and resets the timer to 25 minutes.
  - **Skip Break**: Starts a 10-minute countdown before reminding you to take a break again.
- **Reset Functionality**: Allows you to reset the timer at any time.

## Requirements

To run this script, you need Python 3.11 installed. You also need to install the required libraries listed in `requirements.txt`.

### Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/imraj569/break_reminder.git
    cd break_reminder
    ```

2. Run the script using:
    ```bash
    python break_reminder.pyw
    ```

## How It Works

1. **Start the Timer**: Click the "Start" button to begin the 25-minute countdown.
2. **Take a Break**: When prompted, click "Take Break" to lock the PC and reset the timer.
3. **Skip Break**: If you're not ready to take a break, click "Skip Break" to start a 10-minute countdown.
4. **Reset Timer**: Use the "Reset" button to reset the timer to its initial state.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [Rajkishor Patra](https://github.com/imraj569/). Feel free to reach out for any questions or feedback!
```

### requirements.txt

```plaintext
tkinter
```

### How to Add Files to Your GitHub Repository

1. **Create the `requirements.txt` file**:
   - Save the content provided above into a file named `requirements.txt`.

2. **Create the `README.md` file**:
   - Save the content provided above into a file named `README.md`.

3. **Push the changes to GitHub**:
   ```bash
   git add README.md requirements.txt break_reminder.pyw
   git commit -m "Added README and requirements.txt for break_reminder.pyw"
   git push origin main
   ```

This should set up your GitHub repository nicely!