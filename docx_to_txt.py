import sys
from docx import Document

def docx_to_txt(docx_path, txt_path, separator):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + separator)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py input.docx output.txt")
        sys.exit(1)

    docx_file = sys.argv[1]
    txt_file = sys.argv[2]

    docx_to_txt(docx_file, txt_file, "")
