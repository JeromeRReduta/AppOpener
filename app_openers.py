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
    


def convert_file_to_commands(csv_file):
    """Converts all values in a csv file into command-line arguments

    Args:
        csv_file (str): path to csv

    Returns:
        list[list[str]]: a nested list of command-line arguments # TODO: make this a flat list
    """
    
    values = csv.reader(csv_file) 
    next(values, None) # skips headers
    return [convert_row_to_commands(row) for row in values]

def convert_row_to_commands(row):
    """Converts one row in the csv to a list of command-line arguments\
    
    WARNING: Not having an app name in the CSV is a FATAL ERROR. If this happens, the program will EXIT.

    Args:
        row (list[str]): one row from a csv.reader iterable

    Returns:
        list[str]: a list of command-line arguments, i.e. ["name url", "name url1," "name url2,"...]
                   if no urls were given, simply returns the name as a command-line argument
    """
    commands = []
    if row[0] is None or row[0].strip == "":
        print("ERROR - NO PROGRAM NAME LISTED")
        exit(-1)
    name = row[0].strip()
    for i in range(1, len(row)):
        if row[i] is None or row[i].strip() == "":
            continue
        arg = row[i].strip()
        commands.append(r'{} "{}"'.format(name, arg)) # Terminal treats ' and " differently - we need ' on the outside or terminal doesn't recognize second line should be treated as one term
    return commands if commands else [name]

def open_all_sites(commands):
    """Runs all given commands through the command line. In this context, it opens all sites
       in the CSV alongside its urls

    Args:
        commands (list[str]): all command-line args
    """
    for command in commands:
        for line in command:
            if line.find("obs64") != -1:
                print("We found an obs bois" + line)
                open_obs(line)
            else:
                Application(backend="uia").start(line)
            
def open_obs(line):
    """opens obs
        
        obs needs specific support because you have to start it from its directory or it won't work

    Args:
        line (str): command-line arg
    """
    obs64_index = line.find("obs64")
    dir, exe = line[0:obs64_index], line[obs64_index:]
    os.system(r'start /d "{}" {}'.format(dir, exe))