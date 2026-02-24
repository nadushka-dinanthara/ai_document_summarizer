import pytesseract
from PIL import Image
import cv2
import numpy as np

# 🔹 Set the full path to your Tesseract executable
# Replace this path with the folder where you installed Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def extract_text(processed_img):
    """
    Takes a preprocessed OpenCV image and returns extracted text using Tesseract OCR.
    """
    try:
        # Convert OpenCV image to PIL format
        pil_img = Image.fromarray(processed_img)
        text = pytesseract.image_to_string(pil_img)
        return text
    except Exception as e:
        print("Error in OCR:", e)
        return ""