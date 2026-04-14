import argparse
from txt_to_docx import txt_to_docx

def main():
    parser = argparse.ArgumentParser(description="Convert TXT to DOCX (split 15MB each if needed)")
    parser.add_argument("txt_file", help="Input TXT file path")
    parser.add_argument("--output-name", required=True, help="Output file name (for small files) or directory name (for large files)")
    args = parser.parse_args()

    txt_to_docxs(args.txt_file, args.output_name)

if __name__ == "__main__":
    main()
