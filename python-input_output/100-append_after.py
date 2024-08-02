#!/usr/bin/python3

"""Are you docuemnted ?"""
def append_after(filename="", search_string="", new_string=""):
    
    """
    Insert a line of text after each a specific string in a file.
    Args:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line.
    Returns:
    None
    Note:
    - The function uses the 'with' statement for file handling.
    - It does not manage file permissions or 'file doesn't exist' exceptions.
    - No modules are imported in this function.
    """
    # Read the file content
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Process the lines and insert new_string after matching lines
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
