# main.py
import streamlit as st
import numpy as np
import cv2
from pdf2image import convert_from_bytes
from src.preprocess import preprocess_image
from src.ocr import extract_text

# Sumy LexRank imports
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Update this path to your poppler bin
POPPLER_PATH = "C:/Users/ACER/Downloads/Release-24.08.0-0/poppler-24.08.0/Library/bin"

st.title("🧾 AI Invoice & Receipt Summarizer")
st.write("Upload an invoice or receipt (PDF or Image) and get an auto-generated summary.")

uploaded_file = st.file_uploader("Choose a file", type=["jpg","png","pdf"])

def summarize_text(text, sentence_count=5):
    """Summarize text using LexRank (sumy)"""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

if uploaded_file:

    raw_text = ""

    # If PDF, convert pages to images
    if uploaded_file.type == "application/pdf":
        pages = convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)
        for page in pages:
            cv_img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)
            processed_img = preprocess_image(cv_img, is_file=False)
            page_text = extract_text(processed_img)
            raw_text += page_text + "\n"
    else:
        # Image file
        processed_img = preprocess_image(uploaded_file, is_file=True)
        raw_text = extract_text(processed_img)

    # Summarize the OCR text automatically
    try:
        summary_text = summarize_text(raw_text, sentence_count=5)
    except Exception:
        # fallback if text too short or error
        summary_text = raw_text

    # Display the summary
    st.subheader(" Summary")
    st.text_area("Summary", summary_text, height=200)