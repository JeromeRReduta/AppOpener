"""Utility methods for app_opener

    Methods: 
        * print_err(message)
        * convert_file_to_commands(csv_file, acc)
        * convert_row_to_commands(row, acc)
        * convert_obs64_to_commands(row, acc)
        * convert_exe_to_commands(row, acc)
"""

import csv
import re

def print_err(message):
    """Prints a message in red text to signify an error

    Args:
        message (str): The message
    """
    
    print(f"\033[91m{message}\033[0m") # The 1st special char makes all text after it red. The 2nd special char resets the following text to white

def convert_file_to_commands(csv_file, acc = []):
    """converts the contents of a csv file to a list of commands for subprocess.run()

    Args:
        csv_file (str): path to csv file
        acc (list, optional): Stores generated commands. Defaults to [].
    """

    values = csv.reader(csv_file) 
    next(values, None) # skips headers
    for row in values:
        convert_row_to_commands(row, acc)

def convert_row_to_commands(row, acc = []):
    """Converts the contents of one row of comma-separated values to a list of commands for subprocess.run

    Args:
        row (list[str]): row of comma-separated values
        acc (list, optional): Stores generated commands. Defaults to [].
    """
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
    """Special-case function for obs64, since for some reason it requires you to
    run it from its directory
    
    Args:
        row (list): comma-separated values (this must be the row corresponding to obs64)
        
        acc (list, optional): Stores commands. Defaults to [].
    """
    name = row[0]
    obs64_index = name.find("obs64")
    dir, exe = name[0:obs64_index-1], name[obs64_index:]
    acc.append(["START", "/D", dir, exe])

def convert_exe_to_commands(row, acc=[]):
    """Converts an executable path (and any urls present) to commands

    Args:
        row (list[str]): comma-separated values
        acc (list, optional): Stores commands. Defaults to [].
    """
    
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