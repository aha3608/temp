import time
import random
import pyautogui
from pypdf import PdfReader

def simulate_human_reading(pdf_path, sec_per_page=28):
    print("Open the PDF in Adobe Acrobat Reader, focus the window, enable continuous scrolling.")
    input("Press Enter when ready... ")
    time.sleep(1)

    try:
        pages = len(PdfReader(pdf_path).pages)
        total_time = pages * sec_per_page
        print(f"{pages} pages → ~{total_time//60} min simulation")
    except:
        total_time = 600
        print("Page count failed → 10 min default")

    print("Starting simulation (Ctrl+C to stop)")
    start = time.time()
    try:
        while time.time() - start < total_time:
            pyautogui.scroll(-random.randint(40, 140))
            time.sleep(random.uniform(0.6, 2.3))

            if random.random() < 0.14:
                time.sleep(random.uniform(4.5, 14))

            if random.random() < 0.11:
                back = random.randint(180, 420)
                pyautogui.scroll(back)
                time.sleep(random.uniform(3.5, 9.5))
                pyautogui.scroll(-back)
    except KeyboardInterrupt:
        pass
    print("Done")

if __name__ == "__main__":
    PDF_FILE = r"C:\Path\To\Your\File.pdf"
    simulate_human_reading(PDF_FILE)
