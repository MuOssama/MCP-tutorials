# tools/read_cv_pdf.py
# MCP Tool 1: Extract text from a CV PDF file

import pdfplumber


def read_cv_pdf(pdf_path: str) -> str:
    """
    Read and extract all text from a CV PDF file.

    Args:
        pdf_path: Absolute or relative path to the PDF file.

    Returns:
        Extracted text content from the PDF.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            pages_text = [page.extract_text() or "" for page in pdf.pages]
        text = "\n".join(pages_text).strip()
        if not text:
            return "ERROR: Could not extract any text (PDF may be image-based)."
        return text
    except FileNotFoundError:
        return f"ERROR: File not found -> {pdf_path}"
    except Exception as e:
        return f"ERROR: {e}"