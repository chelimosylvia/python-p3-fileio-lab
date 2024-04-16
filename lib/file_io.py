from pathlib import Path

def write_file(file_name, file_content):
    try:
        file_path = Path(file_name).with_suffix('.txt')
        with open(str(file_path), 'w') as file:
            file.write(file_content)
        print("File '{}' successfully written.".format(file_name))
    except Exception as e:
        print("An error occurred while writing the file:", str(e))

def append_file(file_name, file_content):
    try:
        file_path = Path(file_name).with_suffix('.txt')
        with open(str(file_path), 'a') as file:
            file.write(file_content)
        print("Content appended to file '{}'.".format(file_name))
    except Exception as e:
        print("An error occurred while appending to the file:", str(e))

def read_file(file_name):
    try:
        file_path = Path(file_name).with_suffix('.txt')
        with open(str(file_path), 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print("An error occurred while reading the file:", str(e))
        return None
