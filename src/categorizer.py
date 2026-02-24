# src/categorizer.py
def categorize_expense(merchant):
    """
    Simple merchant-based categorization
    You can extend this later with ML
    """
    merchant = merchant.lower()
    if any(x in merchant for x in ["uber", "ola", "taxi", "bus"]):
        return "Transport"
    elif any(x in merchant for x in ["kfc", "dominos", "restaurant", "cafe"]):
        return "Food"
    elif any(x in merchant for x in ["dialog", "mobitel", "internet", "bill"]):
        return "Utilities"
    else:
        return "Other"