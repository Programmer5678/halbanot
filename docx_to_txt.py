#!/usr/bin/env python3
import sys
import os
import docx2txt

def docx_to_txt(docx_path, txt_path):
    # doc = Document(docx_path)
    # with open(txt_path, 'a', buffering=65536, encoding="utf-8") as f:
    #     print(f"Converting {docx_path} -> {txt_path}")
    #     for index, para in enumerate(doc.paragraphs):
    #         print("para number", index, " length", len(para.text))
    #         f.write(para.text)
    
    with open(txt_path, 'a', buffering=65536, encoding="utf-8") as f:
        
        with open(docx_path, 'rb') as docx_file:
            
            print(f"Converting {docx_path} -> {txt_path}")
            doc = docx2txt.process(docx_file)
            print("writing length", len(doc))
            f.write(doc)
        

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
                print("Appended", fname, "to", output_path)
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
