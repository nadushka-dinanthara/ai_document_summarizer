import streamlit as st
from src.preprocess import preprocess_image
from src.ocr import extract_text
from src.summarizer import summarize_text
from PIL import Image
import numpy as np
import cv2

st.title("📄 AI Document Scanner & Summarizer")
st.write("Upload your document image (jpg/png) or PDF, and get a summary instantly!")

# File upload
uploaded_file = st.file_uploader("Upload document", type=["jpg","png"])

if uploaded_file:
    # Preprocess the uploaded image
    processed_img = preprocess_image(uploaded_file)

    # OCR: extract text
    text = extract_text(processed_img)

    # Summarize text
    summary = summarize_text(text)

    # Display results
    st.subheader("Extracted Text")
    st.text_area("Text from your document", text, height=300)

    st.subheader("Summary")
    st.text_area("Summary", summary, height=200)

    # Optional: show processed image
    st.image(processed_img, caption="Processed Image", use_column_width=True)