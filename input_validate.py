import os

def validate_parent_dir(path):
    if not os.path.exists(os.path.dirname((path))):
        raise Exception(f"{path} parent doesnt exist")

def validate_is_file(path):
    if not os.path.isfile(path):
        raise Exception(f"{path} isnt file")

def validate_abs_path(path: str) -> None:
    if not os.path.isabs(path):
        raise ValueError(f"Path is not absolute: {path}")

def validate_exists(path):
    if not os.path.exists(path):
        raise Exception(f"{path} doesnt exist")