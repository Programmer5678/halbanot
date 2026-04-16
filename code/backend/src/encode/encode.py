from src.zip import zip
from src.base64encode.base64encode import encode_file_to_base64
from src.txt_to_docx.txt_to_docx import txt_to_docxs
from src.encode.input_validate import validate_parent_dir, validate_is_file,validate_abs_path

def validate_input(input_path, output_path):
     validate_abs_path(input_path)
     validate_abs_path(output_path)

     validate_is_file(input_path)
     validate_parent_dir(output_path)

def encode(input_path: str, output_path: str):

     validate_input(input_path, output_path)

     zip_path = "/tmp/b64_zip"
     zip(input_path, zip_path)

     base64_path = "/tmp/b64_encoded"
     encode_file_to_base64(zip_path, base64_path, False)

     return txt_to_docxs(base64_path, output_path )





# encode("/home/ruz/coding/backend-stuff/halbanot/playground/file.txt",
#        "/home/ruz/coding/backend-stuff/halbanot/playground/s_file.txt.zip.b64"
#        )
