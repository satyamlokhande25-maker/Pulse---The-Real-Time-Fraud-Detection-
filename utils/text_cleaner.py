# utils/text_cleaner.py

def clean_text(text: str) -> str:
    """
    Basic text cleaning: lowercase + strip whitespace
    """
    return text.lower().strip()
