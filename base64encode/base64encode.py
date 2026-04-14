
import base64
import os
import sys



def encode_file_to_base64(input_path: str, output_path: str, add_pem_headers: bool):
    # if not os.path.isfile(input_path):
    #     print(f"Error: File '{input_path}' does not exist.", file=sys.stderr)
    #     sys.exit(1)

    with open(input_path, "rb") as fin, open(output_path, "wb") as fout:
        base64.encode(fin, fout)







