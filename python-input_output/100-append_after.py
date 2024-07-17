#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string in a file.

    Args:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line.
    new_string (str): The string to insert after each line containing the search string.

    Returns:
    None

    This function reads the content of the specified file, searches for lines
    containing the search string, and inserts the new string after each matching line.
    The modified content is then written back to the file.

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
