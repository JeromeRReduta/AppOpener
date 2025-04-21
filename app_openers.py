"""Utility methods for app_opener

    Methods: 
        * convert_file_to_commands(csv_file)
        * convert_row_to_commands(row)
        * open_all_sites(commands)
        * open_obs(line)
"""

from pywinauto.application import Application
import csv
import os
import re
import subprocess

""" TODO:

1. new docstrings
2. new readme describing the change and telling ppl they can go to pywinauto branch if they want old functionality and no more dependencies (beyond stdlib)
3. clean up code
4. push


"""

def print_err(message):
    print(f"\033[91m{message}\033[0m")

def convert_file_to_commands(csv_file, acc = []):

    values = csv.reader(csv_file) 
    next(values, None) # skips headers
    for row in values:
        convert_row_to_commands(row, acc)

def convert_row_to_commands(row, acc = []):
    name = row[0]
    if name is None:
        print_err("Error - no executable path given")
        return
    is_executable = bool(re.search(".exe$", row[0], re.IGNORECASE))
    if not is_executable:
        print_err(f"Error: {name} is not an executable path")
        return
    name = name.strip()
    is_obs64 = name.find("obs64") != -1
    if is_obs64:
        convert_obs64_to_commands(row, acc)
        return
    convert_exe_to_commands(row, acc)
    
def convert_obs64_to_commands(row, acc=[]):
    name = row[0]
    obs64_index = name.find("obs64")
    dir, exe = name[0:obs64_index-1], name[obs64_index:]
    acc.append(["START", "/D", dir, exe])

def convert_exe_to_commands(row, acc=[]):
    has_added_anything = False
    name = row[0].strip()
    for i in range(1, len(row)):
        arg = row[i]
        if arg is None:
            continue
        arg = arg.strip()
        if arg == "":
            continue
        acc.append([name, arg]) # Hey don't put ampersands in a url
        has_added_anything = True
    if not has_added_anything:
        acc.append([name])

def open_all_sites(commands):
    for command in commands:
        print(command)
        subprocess.run(command, shell=True)