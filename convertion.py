import os
import textract
from pdfminer.high_level import extract_text
from docx import Document

def convert_pdf_to_txt(file_path):
    text = extract_text(file_path)
    return text

def convert_docx_to_txt(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    return '\n'.join(paragraphs)

def convert_to_txt(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Convert .pdf file to .txt
    if file_extension == '.pdf':
        text = convert_pdf_to_txt(file_path)
    # Convert .docx file to .txt
    elif file_extension == '.docx':
        text = convert_docx_to_txt(file_path)
    else:
        print(f"Skipping {file_path}. Invalid file format.")
        return

    # Create a .txt file with the same name as the original file
    output_file_path = os.path.splitext(file_path)[0] + '.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Converted {file_path} to {output_file_path}")

def convert_documents_to_txt():
    # Get all files in the current directory
    files = os.listdir()
    for file_name in files:
        # Check if the file is a .pdf or .docx file
        if file_name.endswith('.pdf') or file_name.endswith('.docx'):
            convert_to_txt(file_name)

# Run the conversion
convert_documents_to_txt()
