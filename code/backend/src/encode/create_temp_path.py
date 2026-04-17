import os

def is_windows():
    return os.name == "nt"

def create_temp_path(name):
    if( is_windows() ):
        return f"C:\\Temp\\{name}"

    else:
        return f"/tmp/{name}"


