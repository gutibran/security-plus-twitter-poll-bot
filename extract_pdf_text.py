import argparse
import json
from pypdf import PdfReader
import sys

def extract_pdf_text(pdf_file_path):
    """Read in a PDF, extract all the text from the PDF, and returns the text as a list. Each element in the list corresponds to a single page."""
    reader = PdfReader(pdf_file_path)
    page_count = len(reader.pages)
    pages = reader.pages
    text = []
    for index, page in enumerate(pages):
        text_ = pages[index].extract_text()
        if text_ != "":
            text.append(text_)
    return text


def export_extracted_text(extracted_text, json_file_path):
    """Dump the list (pages) of extracted text into a JSON file."""
    with open(json_file_path, "w") as json_file:
        json.dump(extracted_text, json_file)


def main():
    pdf_file_path = input("Enter the path of the PDF to extract: ")
    json_file_path = input("Enter the path of the JSON file to write the extracted to: ")
    print(f"Extracting text from {pdf_file_path}")
    extracted_text = extract_pdf_text(pdf_file_path)
    export_extracted_text(extracted_text, json_file_path)
    print("Done.")


if __name__ == "__main__":
    main()