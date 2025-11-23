from io import BytesIO
from pypdf import PdfReader

def extract_text_from_pdf(pdf_file: BytesIO) -> str:
    """
    Extracts text from a PDF file using pypdf.

    Args:
        pdf_file: A BytesIO object containing the PDF file's content.

    Returns:
        The extracted text as a single string.
    """
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
