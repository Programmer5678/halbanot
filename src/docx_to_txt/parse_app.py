from docx_to_txt import docxs_to_txt
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py input.docx_or_dir output.txt")
        sys.exit(1)

    inp = sys.argv[1]
    out = sys.argv[2]

    docxs_to_txt(inp, out)