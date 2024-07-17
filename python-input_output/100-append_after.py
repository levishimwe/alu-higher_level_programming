#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    # Read the file content
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Process the lines and insert new_string after matching lines
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

                
