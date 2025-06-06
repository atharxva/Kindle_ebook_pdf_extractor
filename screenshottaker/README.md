# Kindle Screenshot Automation

This script automates taking screenshots from the Kindle app on macOS. It allows you to take screenshots using a hotkey and automatically turns pages.

## Requirements

- Python 3.6 or higher
- macOS
- Kindle app installed

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open the Kindle app and navigate to the page you want to start capturing from
2. Run the script:
```bash
python kindle_screenshot.py
```
3. Press `Ctrl+Shift+K` (or your configured hotkey) to take a screenshot
4. Press `q` to quit the script

## Features

- Takes screenshots with timestamp-based filenames
- Stores screenshots in a dedicated folder
- Configurable hotkey for taking screenshots
- Automatic page turning functionality

## Configuration

You can modify the following settings in `kindle_screenshot.py`:

- `HOTKEY`: Change the hotkey combination (default: "ctrl+shift+k")
- `PAGE_TURN_DELAY`: Adjust the delay between page turns (default: 2 seconds)
- `SCREENSHOT_FOLDER`: Change the folder where screenshots are saved (default: "kindle_screenshots")

## Notes

- Make sure the Kindle app is in focus when taking screenshots
- The script requires accessibility permissions to control the keyboard
- Screenshots are saved in the `kindle_screenshots` folder with timestamps 