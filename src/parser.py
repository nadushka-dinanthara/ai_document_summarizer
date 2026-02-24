# src/parser.py
import re
from datetime import datetime

def extract_invoice_info(text):
    """
    Extracts structured info from raw OCR text
    """
    # Example regex patterns
    date_pattern = r'\b(?:\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4})\b'
    amount_pattern = r'\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b'
    
    # Extract first date found
    dates = re.findall(date_pattern, text)
    date = dates[0] if dates else "Not found"
    
    # Extract all amounts, pick largest (assuming total)
    amounts = re.findall(amount_pattern, text.replace(',', ''))
    total = max([float(a) for a in amounts]) if amounts else 0.0
    
    # Merchant: first line assuming it's the header
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    merchant = lines[0] if lines else "Unknown"
    
    return {
        "merchant": merchant,
        "date": date,
        "total": total
    }