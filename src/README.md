📄 AI Document Scanner & Summarizer

An interactive Streamlit-based ML application that allows users to upload images or PDF documents, extract text using OCR, and generate a concise summary automatically.

This project combines:

✔ Computer Vision (OpenCV)
✔ Optical Character Recognition (Tesseract OCR)
✔ Natural Language Processing (Text Summarization)
✔ Interactive UI (Streamlit)

🚀 Features

Upload JPG / PNG images

Upload PDF documents (multi-page supported)

Automatic PDF → Image conversion

Image preprocessing for improved OCR accuracy

Text extraction via Tesseract OCR

Extractive text summarization using LexRank

Clean & simple UI

📂 Project Structure
ai_document_summarizer/
│
├── main.py
├── requirements.txt
│
└── src/
    ├── preprocess.py
    ├── ocr.py
    └── summarizer.py
⚙️ Requirements

Python 3.10+

Tesseract OCR (Windows)

Poppler (for PDF processing)

🛠 Installation Guide (Windows)
1️⃣ Clone the Repository
git clone <your-repo-url>
cd ai_document_summarizer
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Python Dependencies
pip install -r requirements.txt
📄 PDF Support Dependency (Poppler)

PDF files are converted to images using pdf2image, which requires Poppler.

✅ Download Poppler

Download from:

https://github.com/oschwartz10612/poppler-windows/releases

Recommended version:

✔ poppler-24.08.0-0.zip

✅ Extract Poppler

Example location:

C:\Users\ACER\Downloads\poppler-24.08.0

Confirm this folder exists:

C:\Users\ACER\Downloads\poppler-24.08.0\bin

Inside bin, you MUST see:

pdfinfo.exe
pdftoppm.exe
✅ Configure Poppler Path in Code

Open main.py and update:

POPPLER_PATH = r"C:\Users\ACER\Downloads\poppler-24.08.0\bin"

⚠ Use your exact extracted location.

🔎 OCR Dependency (Tesseract)

Text extraction relies on Tesseract OCR.

✅ Install Tesseract

Download Windows installer:

https://github.com/UB-Mannheim/tesseract/wiki

Install with default settings.

Default path:

C:\Program Files\Tesseract-OCR\tesseract.exe
✅ Configure Tesseract Path

Open src/ocr.py and confirm:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶ Running the Application

Activate virtual environment:

venv\Scripts\activate

Run Streamlit:

streamlit run main.py

Browser will open automatically.

📌 How It Works

User uploads Image / PDF

PDFs are converted to images via Poppler

Images are preprocessed using OpenCV

Tesseract extracts text

NLP summarizer generates summary

UI displays results

🧠 ML / NLP Components

OCR Engine → Tesseract OCR

Summarization Model → LexRank (Extractive)

Image Processing → OpenCV adaptive thresholding