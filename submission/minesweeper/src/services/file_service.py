'''
    Description: Reads from a given file path.
    Parameters:
        file_path: A string representing the file path.
    Returns:
        A string representing the content of the file.
'''
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

'''
    Description: Writes to a given file path.
    Parameters:
        file_path: A string representing the file path.
        content: A string representing the content to write to the file.
'''
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
