from docx_to_txt import process_nested_path
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py input.docx_or_dir output.txt")
        sys.exit(1)

    inp = sys.argv[1]
    out = sys.argv[2]

    process_nested_path(inp, out)