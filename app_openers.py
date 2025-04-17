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

def convert_file_to_commands(csv_file, acc = []):
    """Converts all values in a csv file into a list of command-line arguments
    
    Args:
        csv_file (str): path to csv
        acc (list, optional): stores generated command-line arguments. Used when parsing the whole file (see convert_file_to_commands) Defaults to [].
    """
    
    values = csv.reader(csv_file) 
    next(values, None) # skips headers
    for row in values:
        convert_row_to_commands(row, acc)

def convert_row_to_commands(row, acc = []):
    """Converts one row of values in a csv file into a list of command-line arguments. Arguments are appended to an accumulator for efficiency
    
    Args:
        row (list[str]): the values in a given row of a csv file
        acc (list, optional): stores generated command-line arguments. Used when parsing the whole file (see convert_file_to_commands) Defaults to [].
    """
    
    is_executable = bool(re.search(".exe$", row[0], re.IGNORECASE))
    if row[0] is None or not is_executable:
        print(f"\033[91mError - cannot process executable path {row[0]}\033[0m") # Weird characters turn this error text red, then changes color back to white
        return
    has_added_anything = False
    name = row[0].strip()
    for i in range(1, len(row)):
        arg = row[i]
        if arg is None:
            continue
        arg = arg.strip()
        if arg == "":
            continue
        acc.append(r'{} "{}"'.format(name, arg)) # Terminal treats ' and " differently - we need ' on the outside or terminal doesn't recognize second line should be treated as one term
        has_added_anything = True
    if not has_added_anything:
        acc.append(name)

def open_all_sites(commands):
    """Runs all given commands through the command line. In this context, it opens all sites
       in the CSV alongside its urls

    Args:
        commands (list[str]): all command-line args
    """
    
    for command in commands:
        is_obs64 = command.find("obs64") != -1
        if is_obs64:
            open_obs64(command)
        else:
            Application(backend="uia").start(command)
            
def open_obs64(line):
    """opens obs
        
        obs needs specific support because you have to start it from its directory or it won't work

    Args:
        line (str): command-line arg
    """
    obs64_index = line.find("obs64")
    dir, exe = line[0:obs64_index], line[obs64_index:]
    os.system(r'start /d "{}" {}'.format(dir, exe))