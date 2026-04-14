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
        

def docxs_to_txt(input_path, output_path):
    """
    Convert DOCX files to a single TXT file. Handles nested directories:
    loops over subdirectories, then files inside each subdirectory.
    
    Args:
        input_path (str): Path to DOCX file or directory containing subdirectories.
        output_path (str): Path to the TXT output file.
    """
    # Delete existing output at the start
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"Deleted existing file: {output_path}")

    if os.path.isdir(input_path):
        # Loop over subdirectories
        for subdir in sorted(os.listdir(input_path)):
            subdir_full = os.path.join(input_path, subdir)
            if os.path.isdir(subdir_full):
                # Loop over files inside subdirectory
                for fname in sorted(os.listdir(subdir_full)):
                    file_full = os.path.join(subdir_full, fname)
                    if os.path.isfile(file_full):
                        docx_to_txt(file_full, output_path)
                        print("Appended", fname, "from", subdir, "to", output_path)
                    else:
                        raise ValueError(f"Expected file but found directory: {file_full}")
            else:
                raise Exception(f"non-directory: {subdir_full}")
        print(f"Appended all nested files in {input_path} to {output_path}")
    else:
        # Single DOCX file
        docx_to_txt(input_path, output_path)
        print(f"Appended {input_path} to {output_path}")


