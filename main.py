import streamlit as st
import numpy as np
import cv2
from pdf2image import convert_from_bytes
from src.preprocess import preprocess_image
from src.ocr import extract_text
from src.summarizer import summarize_text

POPPLER_PATH = "C:/Users/ACER/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin"

st.title("📄 AI Document Scanner & Summarizer")
st.write("Upload an image or PDF document")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["jpg", "png", "pdf"]
)

if uploaded_file:

    text_all_pages = ""

    # ---------- PDF Handling ----------
    if uploaded_file.type == "application/pdf":

        pages = convert_from_bytes(
            uploaded_file.read(),
            poppler_path=POPPLER_PATH
        )

        st.success(f"PDF Loaded ({len(pages)} pages)")

        for page in pages:
            # Convert PIL → OpenCV
            cv_img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

            processed_img = preprocess_image(cv_img, is_file=False)

            page_text = extract_text(processed_img)

            text_all_pages += page_text + "\n\n"

    # ---------- Image Handling ----------
    else:
        processed_img = preprocess_image(uploaded_file, is_file=True)
        text_all_pages = extract_text(processed_img)

    # ---------- Summarization ----------
    summary = summarize_text(text_all_pages)

    # ---------- UI Output ----------
    st.subheader("Extracted Text")
    st.text_area("OCR Output", text_all_pages, height=300)

    st.subheader("Summary")
    st.text_area("Summary", summary, height=200)