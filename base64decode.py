import argparse
import base64

def decode_file_from_base64(input_path: str, output_path: str):
    """Decode a Base64-encoded file and save the result to a new file."""
    with open(input_path, "rb") as fin, open(output_path, "wb") as fout:
        base64.decode(fin, fout)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Base64-decode a file and save the result to a new file."
    )
    parser.add_argument(
        "input",
        help="Path to the Base64-encoded input file"
    )
    parser.add_argument(
        "output",
        help="Path to save the decoded output file"
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    decode_file_from_base64(args.input, args.output)
