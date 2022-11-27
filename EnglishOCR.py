import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"F:\Users\salma\AppData\Local\Programs\OCR tesseract\tesseract.exe"
def convertToEngText(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang="en")
    return text

