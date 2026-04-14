from base64encode.base64encode import encode_file_to_base64
from txt_to_docx.txt_to_docx import txt_to_docxs


def encode(input_path: str, output_path: str):

     base64_path = "/tmp/b64_encoded"
     encode_file_to_base64(input_path, base64_path, False)
     txt_to_docxs(base64_path, output_path )

encode("file.txt.zip", "s_file.txt.zip.b64")



