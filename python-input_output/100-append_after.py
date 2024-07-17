#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
    filename (str): The name of the file.
    search_string (str): The string to search for within each line of the file.
    new_string (str): The string to append after each line that contains the search string.

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

# Example usage:
# append_after("example.txt", "world", "This is the appended line")
