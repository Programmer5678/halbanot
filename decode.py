from zip import unzip
from base64decode.base64decode import decode_file_from_base64
from docx_to_txt.docx_to_txt import docxs_to_txt
from input_validate import validate_parent_dir, validate_exists,validate_abs_path

def validate_input(input_path, output_path):
    validate_abs_path(input_path)
    validate_abs_path(output_path)

    validate_exists(input_path)
    validate_parent_dir(output_path)

def decode(input_path: str, output_path: str):

    validate_input(input_path, output_path)

    input_path_decoded = "/tmp/docx_decoded"
    docxs_to_txt(input_path, input_path_decoded )

    base64_decoded = "/tmp/base64_decoded"
    decode_file_from_base64(input_path_decoded , base64_decoded)

    unzip(base64_decoded, output_path)


decode("/home/ruz/coding/backend-stuff/halbanot/playground/s_file.txt.zip.b64.docx",
       "/home/ruz/coding/backend-stuff/halbanot/playground/s")

