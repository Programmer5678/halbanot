import base64encode
import argparse
from base64encode import encode_file_to_base64

def str2bool(v):
    if isinstance(v, bool):
        return v
    v_lower = v.lower()
    if v_lower == "true":
        return True
    elif v_lower == "false":
        return False
    else:
        raise argparse.ArgumentTypeError("Expected 'true' or 'false'")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Base64-encode a file and save the result to a new file, optionally adding PEM headers."
    )
    parser.add_argument(
        "input",
        help="Path to the input file to encode"
    )
    parser.add_argument(
        "output",
        help="Path to save the encoded output"
    )
    parser.add_argument(
        "--add-pem-headers",
        required=True,
        type=str2bool,
        help="Specify 'true' to add PEM headers, 'false' otherwise."
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    encode_file_to_base64(args.input, args.output, args.add_pem_headers)