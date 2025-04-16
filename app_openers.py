from pywinauto.application import Application
import csv
from argparse import ArgumentParser
import os

description = """An app that opens up a list of files in a CSV, alongside any URLS.

                 For example, this app can open several Chrome tabs at given links."""

def get_csv_path():
    parser = ArgumentParser(description=description)
    parser.add_argument("csv_path")
    return parser.parse_args().csv_path

def convert_file_to_commands(csv_file):
    values = csv.reader(csv_file) 
    next(values, None) # skips headers
    return [convert_row_to_commands(row) for row in values]

def convert_row_to_commands(row):
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
    for command in commands:
        for line in command:
            if line.find("obs64") != -1:
                print("We found an obs bois" + line)
                open_obs(line)
            else:
                Application(backend="uia").start(line)
            
def open_obs(line):
    """obs needs specific support because you have to start it from its directory or it won't work"""
    obs64_index = line.find("obs64")
    dir, exe = line[0:obs64_index], line[obs64_index:]
    os.system(r'start /d "{}" {}'.format(dir, exe))