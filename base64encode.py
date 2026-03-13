import argparse
import base64
import os
import sys

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

def encode_file_to_base64(input_path: str, output_path: str, add_pem_headers: bool):
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # with open(input_path, "rb") as infile:
    #     encoded_bytes = base64.b64encode(infile.read())

    # if add_pem_headers:
    #     pem_content = (
    #         "-----BEGIN CERTIFICATE-----\n" +
    #         encoded_bytes.decode('ascii') +
    #         "\n-----END CERTIFICATE-----\n"
    #     )
    #     with open(output_path, "w", encoding="ascii") as outfile:
    #         outfile.write(pem_content)
    # else:
    #     with open(output_path, "wb") as outfile:
    #         outfile.write(encoded_bytes)
    
    
    with open(input_path, "rb") as fin, open(output_path, "wb") as fout:
        base64.encode(fin, fout)

    print(f"Base64 encoded file saved to: {output_path}")

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
