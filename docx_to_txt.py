#!/usr/bin/env python3
import sys
import os
from docx import Document

def docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    with open(txt_path, 'ab', buffering=0) as f:
        print(f"Converting {docx_path} -> {txt_path}")
        for index, para in enumerate(doc.paragraphs):
            print("para number", index)
            s = para.text
            f.write(s.encode('utf-8'))

def process_path(input_path, output_path):
    # Delete the output file at the start if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"Deleted existing file: {output_path}")

    if os.path.isdir(input_path):
        # Sort directory contents alphabetically
        for fname in sorted(os.listdir(input_path)):
            docx_full = os.path.join(input_path, fname)
            if os.path.isfile(docx_full):
                docx_to_txt(docx_full, output_path)
                print("Appended", fname)
            else:
                raise ValueError(f"Expected file but found directory: {docx_full}")
        print(f"Appended all files in {input_path} to {output_path}") 
    else:
        docx_to_txt(input_path, output_path)
        print(f"Appended {input_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py input.docx_or_dir output.txt")
        sys.exit(1)

    inp = sys.argv[1]
    out = sys.argv[2]   

    process_path(inp, out)
