from PIL import Image
from tkinter import Tk, filedialog
import pytesseract
import os


try:
    pytesseract.get_tesseract_version()
except pytesseract.TesseractNotFoundError:
    print("❌ Tesseract is not in your PATH or not installed.")

root = Tk()
root.withdraw() #closes TK window
print("Select your text image...")
image_path = filedialog.askopenfilename(
  title="Select An Image:",
  filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
  )

print(f"Got it!: ", end="")
print(image_path)

