from PIL import Image
from tkinter import Tk, filedialog
import pytesseract
import os, sys, emoji, time

##FUNCTIONS

#gives CommandLine response a human touch
#iterates through text and slowly types
#gaurantees a new line after text is done
def printSlow(text, delay=.05, end="\n", flush=True):
  for char in text:
    print(char, end="", flush=flush)
    time.sleep(delay)
  print(end=end, flush=flush)
#recursive function giving user option to overwrite .py file
#while also error handling invalid inputs
def userinputResponse():
  while True:
    user_input = printSlow(input("You already have an image_text.py, do you want to overwrite it? Y/N: "))
    if user_input.lower() == "y":
      with open("image_text.py", "w") as image_text:
        image_text.write(text)
      printSlow(emoji.emojize(":check_mark_button: Overwritten existing image_text.py file..."))
      sys.exit()
    elif user_input.lower() == "n":
      programShutdown()
    else:
      printSlow(f"Sorry, but {user_input} isn't a valid input")
    userinputResponse()
#throws some attitude when it has to exit
def programShutdown(self):
    printSlow("Uh...", flush=True, end=" ")
    time.sleep(1)
    printSlow("Okay...", flush=True, end=" ")
    time.sleep(1)
    printSlow("shutting down... delete the current image_text.py and try again!")
    sys.exit()
## END of FUNCTIONS

## MAIN-RUN

#error handles if image_scraper is not installed
try:
  pytesseract.get_tesseract_version()
except pytesseract.TesseractNotFoundError:
  print(emoji.emojize(":cross_mark_button: Tesseract is not in your PATH or not installed."))
  sys.exit()

root = Tk()
root.withdraw() #closes TK window
printSlow("Select your text image...")
#opens local window for user to select image

image_path = filedialog.askopenfilename(
  title="Choose A Screenshot of Python Code (nothing more...nothing less)",
  filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
  )
if not image_path: 
  printSlow(emoji.emojize(":cross_mark_button: No file selected, shutting down..."))
  sys.exit()

#checks to see if the image_path exists
#if True, confirm and display PATH
#if False, display error and exit
try:
    image = Image.open(image_path)
except FileNotFoundError:
    printSlow(f"Image path '{image_path}' not found...")
    sys.exit()
printSlow(f"Got it!: ", end="")
printSlow(image_path)

#converts image to text
text = pytesseract.image_to_string(image)
#creates a new file, writes text to file, then closes
try:
  image_text = open("image_text.py","x")
  image_text.write(text)
  printSlow(f"Your text file was written into image_text.py")
  image_text.close()
  #OVERWITE-block... if file already exists, gives option to overwrite
except FileExistsError:
  userinputResponse()
 
    
   
    
  

    


