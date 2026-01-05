import pdfplumber

def pdf_to_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text

# Example usage
#pdf_text = pdf_to_text("example.pdf")
#print(pdf_text)
