import zipfile
import os


def zip(input_path, output_path):
    with zipfile.ZipFile(output_path, "w") as z:
        z.write(input_path,
                arcname=os.path.basename(input_path)
                #Makes sure we use relative path otherwise zip will store the entire path so
                # when decompress -> decomp/dir1/dir2/dir3/file.txt
                )

def unzip(input_path, output_path):
    with zipfile.ZipFile(input_path, "r") as z:
        z.extractall(output_path)
