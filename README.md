Here’s a **detailed and easy-to-understand README** for your Kindle screenshot automation script:

---

# 📚 Kindle Screenshot Automation Tool

This Python script automates the process of capturing screenshots of Kindle pages. It simulates turning pages and saving each screenshot with a timestamp. Ideal for archiving or studying purposes (note: respect copyright laws!).

---

## 🔧 Features

* 📸 Automatically captures Kindle screenshots.
* ⏩ Turns pages using keyboard automation.
* 🗂️ Organizes screenshots in a dedicated folder.
* 🖱️ Start/stop automation using `F12` and `Esc`.

---

## 🖥️ Requirements

* Python 3.6+
* Modules:

  * `pyautogui`
  * `pynput`
  * `Pillow`

Install dependencies via pip:

```bash
pip install pyautogui pynput pillow
```

---

## 📂 Folder Structure

Screenshots are saved in a folder named `kindle_screenshots` in the same directory as the script.

---

## ▶️ How It Works

1. **Start the script** and switch to your Kindle window (make sure it’s maximized).
2. **Press `F12`** to start the screenshot automation.
3. The script will:

   * Take a screenshot
   * Simulate a right arrow key press to turn the page
   * Repeat until you press `Esc`
4. **Press `Esc`** to stop the automation.

Each screenshot is saved with a filename like:

```
kindle_page_1_20250606_211530.png
```

---

## 📜 Code Overview

| Function                     | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| `create_screenshot_folder()` | Creates the output folder if not already present.                |
| `take_screenshot(page_num)`  | Captures and saves a screenshot of the current screen.           |
| `turn_page()`                | Simulates pressing the right arrow key to flip to the next page. |
| `on_press(key)`              | Listens for `F12` (start) and `Esc` (stop) hotkeys.              |
| `start_automation()`         | The main loop that runs while automation is active.              |
| `main()`                     | Entry point that sets up the listener and user instructions.     |

---

## ⚙️ Customization

You can tweak these two parameters for different speeds:

```python
PAGE_TURN_DELAY = 0.5        # Delay after turning page (in seconds)
SCREENSHOT_DELAY = 0.2       # Delay after taking screenshot (in seconds)
```

If your Kindle app takes time to load a page, increase `PAGE_TURN_DELAY`.

---

## 🚨 Notes

* Ensure Kindle is **the active window** before starting.
* Works best with Kindle in **full screen mode** for consistent screenshots.
* The script captures **the entire screen**, so position the Kindle app properly.

---

## 🧠 Example Usage

```bash
python kindle_screenshot_automation.py
```

Then follow the on-screen instructions:

```
Kindle Screenshot Automation
Switch to the Kindle app window.
Press F12 to start automation. Press Esc to stop.
```

---

## 📬 Feedback

Have suggestions or need help? Feel free to reach out or open an issue!

---

