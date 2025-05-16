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
    printSlow("You already have an image_text.py, do you want to overwrite it? Y/N: ", end="")
    user_input = input()
    if user_input.lower() == "y":
      with open("image_text.py", "w") as image_text:
        image_text.write(text)
      printSlow(emoji.emojize(":check_mark_button: Overwritten existing image_text.py file..."))
      sys.exit()
    elif user_input.lower() == "n":
      programShutdown()
    else:
      printSlow(f"Sorry, but '{user_input}' isn't a valid input")
    userinputResponse()
    
#throws some attitude when it has to exit
def programShutdown():
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
  
#creates instance of TKinter
root = Tk()
root.withdraw() #closes TK window
printSlow("Select your text image...")
#declaring valid file extensions
valid_extensions = [".png",".jpg",".jpeg",".bmp",".tiff"]
#opening local file storage for user to select image
image_path = filedialog.askopenfilename(
  title="Choose A Screenshot of Python Code (nothing more...nothing less)",
  filetypes=[(f"Image files", "*.png *.jpg *.bmp *.tifff")]
  )
_,extension = os.path.splitext(image_path)
#quits if image_path doesn't exist or doesn't match the proper file extensions
if not image_path: 
  printSlow(emoji.emojize(":cross_mark_button: No file selected, shutting down..."))
  sys.exit()
elif extension.lower() not in valid_extensions:
  printSlow(emoji.emojize(f":cross_mark_button: The file you selected doesn't have a photo extension {valid_extensions} double check and try again"))
  sys.exit()

#uses Image to create actual image variable
#if True, confirm and display image's PATH and move on
#if False, display error and exit
try:
    image = Image.open(image_path)
except FileNotFoundError:
    printSlow(f"Image path '{image_path}' not found...")
    sys.exit()
printSlow(f"Got it!: ", end="")
printSlow(image_path)

#converts image to text and checks if there's any valid text
text = pytesseract.image_to_string(image)
if not text: 
  printSlow("Looks like the photo you selected doesn't have any readable text, sorry!")
  printSlow("Shutting down...")
  sys.exit()
  
#gives user option to choose extension, then creates
#a new file, writes text to file, then closes
try:
  acceptable_answers = {
    ".js javascript JavaScript JAVASCRIPT js": ".js", 
    ".py py python Python PYTHON":".py"
  }
  
  while True:
    printSlow("So, do you want a .py or .js extension?: ", end="")
    user_input = input().lower()
    
    for key, extension in acceptable_answers.items():
      if user_input in key.split():
        found=True
        with open(f"image_text{extension}", "x") as image_text:
          image_text.write(text)
          
        printSlow("Okay one sec...", end="")
        time.sleep(2)
        printSlow("Okie dokie!")
        time.sleep(0.5)
        printSlow(f"Your text file was written into image_text.py")
        sys.exit()
        
    printSlow("Ugh...", end="")
    time.sleep(1.5)
    printSlow("Listen...", end="")
    time.sleep(1.5)
    printSlow("We both know that input isn't gonna work...")
        
      
        
  
  #OVERWITE-block... if file already exists, gives option to overwrite
except FileExistsError:
  userinputResponse()
 
    
   
    
  

    


