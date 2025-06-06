
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


# 🖼️📄 Image to PDF Converter

This Python script converts a folder of images into a multi-page **PDF file**, with each image neatly centered and scaled to fit a standard **letter-sized** page.

Perfect for compiling screenshots, scanned documents, or photo albums into a single PDF!

---

## ✅ Features

* 🗂️ Converts all images in a folder into a PDF
* 🔢 Sorts images by **creation time**
* 📏 Automatically resizes and centers images on **letter-sized pages**
* 🧼 Temporary files are cleaned up automatically
* 🧠 Simple CLI usage with helpful logs

---

## 🧰 Requirements

Make sure you have Python 3 installed and the following libraries:

```bash
pip install pillow reportlab
```

---

## 📂 Input Format

Supported image formats:

* `.png`
* `.jpg`
* `.jpeg`
* `.gif`
* `.bmp`

All images in the folder will be processed **in order of creation time**.

---

## ▶️ How to Use

### 🔧 Command-Line Usage

```bash
python image_to_pdf.py <input_folder> <output_pdf>
```

### Example:

```bash
python image_to_pdf.py kindle_screenshots output.pdf
```

This will:

* Look for images in the `kindle_screenshots/` folder
* Create a `output.pdf` with all images added page-by-page

---

## 🔍 Behind the Scenes

| Function                         | Description                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| `get_creation_time(filepath)`    | Returns the creation timestamp for sorting images.                                      |
| `convert_images_to_pdf()`        | The main function that opens each image, scales it, centers it, and adds it to the PDF. |
| `Image.open(...).convert('RGB')` | Ensures the image is compatible with the PDF format.                                    |
| `canvas.Canvas(...).drawImage()` | Handles placing the image into a new page of the PDF.                                   |

Images are scaled to **fit** the page while preserving their **aspect ratio**.

---

## 📌 Output

* PDF pages are **letter-sized** (`8.5in x 11in`)
* Each image is:

  * Resized to fit the page
  * Centered with small margins
  * Added to a new page in the final PDF

---

## ⚠️ Notes

* Make sure your input folder exists and contains images.
* The script temporarily saves resized images as `temp_x.jpg`, which are deleted automatically after processing.
* Large images are resized to prevent PDF bloat.

---

## 📬 Example Output Log

```
Processing 10 images...
Processing image 1/10: kindle_page_1.png
Processing image 2/10: kindle_page_2.png
...
PDF created successfully: output.pdf
Total images processed: 10
```

---

## 📎 License

Feel free to use or modify this script for personal or educational purposes. Always credit original sources when distributing.

---

##Feel free to rach out if you face any issues 
atharvajadhavlm10@gmail.com
