import sys
from docx import Document

# def txt_to_docx(txt_path, docx_path):
#     if not os.path.exists(txt_path):
#         print(f"Error: File '{txt_path}' not found.")
#         return



#     with open(txt_path, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     doc = Document()
#     for line in lines:
#         doc.add_paragraph(line.rstrip())

#     doc.save(docx_path)
#     print(f"Saved DOCX to: {docx_path}")


def txt_to_docx(txt_path, docx_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    doc = Document()
    doc.add_paragraph(content)
    doc.save(docx_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python txt_to_docx.py input.txt output.docx")
        sys.exit(1)

    txt_file = sys.argv[1]
    docx_file = sys.argv[2]

    txt_to_docx(txt_file, docx_file)
