from base64decode.base64decode import decode_file_from_base64
from docx_to_txt.docx_to_txt import docxs_to_txt

def decode(input_path: str, output_path: str):

    input_path_decoded = "/tmp/docx_decoded"
    docxs_to_txt(input_path, input_path_decoded )

    decode_file_from_base64(input_path_decoded , output_path)

decode("s_file.txt.zip.b64.docx", "s_file.txt.zip")

