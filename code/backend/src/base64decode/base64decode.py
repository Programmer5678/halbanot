
import base64

def decode_file_from_base64(input_path: str, output_path: str):
    """Decode a Base64-encoded file and save the result to a new file."""
    with open(input_path, "rb") as fin, open(output_path, "wb") as fout:
        base64.decode(fin, fout)


