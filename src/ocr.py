import pytesseract
from PIL import Image

# ✅ CHANGE if Tesseract installed elsewhere
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def extract_text(processed_img):
    try:
        pil_img = Image.fromarray(processed_img)
        text = pytesseract.image_to_string(pil_img)
        return text
    except Exception as e:
        print("OCR Error:", e)
        return ""