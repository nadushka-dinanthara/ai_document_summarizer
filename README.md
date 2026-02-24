# 🧾 AI Invoice & Receipt Summarizer

A smart app that **reads invoices and receipts (PDF or images)** and generates a **human-readable summary automatically** using OCR and LexRank-based text summarization.  

No manual input required — just upload a file and get a clean, concise summary in seconds.


## 🔹 Features

- Upload **image files** (`.jpg`, `.png`) or **PDF invoices**.  
- Automatically extract text using **Tesseract OCR**.  
- Generate **natural paragraph summaries** using **LexRank** (via `sumy`).  
- Multi-page PDF support.  
- Fully automatic — no manual formatting needed.  

---

## 🔹 How It Works

1. **Upload** an invoice or receipt.  
2. If it’s a PDF, each page is converted to an image.  
3. OCR (**Tesseract**) reads text from the image.  
4. LexRank (**Sumy**) generates a **concise summary paragraph**.  
5. The summary is displayed directly in the app.

---

## 🔹 Example

**Input:** An image or PDF of a receipt  

**Output (summary):**

> "This invoice is from KFC Colombo, dated 22/02/2026. The total amount paid is LKR 1,450.00, which falls under the category 'Food'. Please refer to the original document for full details."

---

## 🔹 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai_document_summarizer.git
cd ai_document_summarizer

Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

Install requirements:

pip install -r requirements.txt

Install Tesseract OCR:

Download: Tesseract

Add Tesseract executable to your PATH, or update tesseract_cmd in your code.

Install Poppler (for PDF to image conversion):

Download: Poppler for Windows

Update POPPLER_PATH in main.py with the bin folder path.

🔹 Run the App
streamlit run main.py

Upload a receipt or invoice (PDF/Image).

The summary paragraph will appear in the app.

🔹 Dependencies

Python 3.9+

Streamlit

OpenCV

NumPy

Pillow

PyTesseract

pdf2image

Sumy
 (LexRank summarization)