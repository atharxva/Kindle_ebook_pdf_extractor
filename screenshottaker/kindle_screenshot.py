import os
import time
import pyautogui
from datetime import datetime
from PIL import Image
from pynput import keyboard

# Configuration
SCREENSHOT_FOLDER = "kindle_screenshots"
PAGE_TURN_DELAY = 0.5  # Reduced from 2 to 0.5 seconds
SCREENSHOT_DELAY = 0.2  # Reduced from 1 to 0.2 seconds

running = False
listener = None

def create_screenshot_folder():
    """Create the screenshot folder if it doesn't exist."""
    if not os.path.exists(SCREENSHOT_FOLDER):
        os.makedirs(SCREENSHOT_FOLDER)

def take_screenshot(page_num):
    """Take a screenshot and save it with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"kindle_page_{page_num}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_FOLDER, filename)
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved: {filepath}")
    time.sleep(SCREENSHOT_DELAY)

def turn_page():
    """Simulate pressing the right arrow key to turn the page."""
    pyautogui.press('right')
    time.sleep(PAGE_TURN_DELAY)

def on_press(key):
    global running
    if key == keyboard.Key.f12 and not running:
        print("F12 pressed: Starting automation...")
        running = True
        start_automation()
    elif key == keyboard.Key.esc and running:
        print("Esc pressed: Stopping automation...")
        running = False
        # Stop listener after automation loop
        return False

def start_automation():
    create_screenshot_folder()
    page_num = 1
    while running:
        take_screenshot(page_num)
        turn_page()
        page_num += 1
    print("Automation stopped.")

def main():
    print("Kindle Screenshot Automation")
    print("Switch to the Kindle app window.")
    print("Press F12 to start automation. Press Esc to stop.")
    global listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main() 