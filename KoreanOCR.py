import pytesseract
import os
from PIL import Image
#한국어 OCR 만들기
pytesseract.pytesseract.tesseract_cmd = r"F:\Users\salma\AppData\Local\Programs\OCR tesseract\tesseract.exe"
#tesseract path
def convertToKoreanText(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang="kor")
    return text



