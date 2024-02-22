import cv2, pytesseract

FILE_NAME = "Japanese.png" # In data directory
LANGUAGE = "jpn"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(f"Data/{FILE_NAME}") # load
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # preprocess
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh, lang=LANGUAGE)
with open("Data/text/data.txt", "w", encoding="utf-8") as file:
    file.write(text)
