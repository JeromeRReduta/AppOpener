"""Given a path to an "App-Opener-CSV" (i.e. a CSV specially formatted for this program) containing executable paths and urls,\
    opens all files w/ their urls
"""

import app_openers as util
from argparse import ArgumentParser

description = """An app that opens up a list of files in a CSV, alongside any URLS.

                 For example, this app can open several Chrome tabs at given links."""

def set_up_args():
    """Sets up command-line arguments for the program

    Returns:
        arg_parser_namespace: Namespace from parser.parse_args(). Since we added
                                   "csv_path" as an argument, namespace.csv_path exists
    """ 
    parser = ArgumentParser(description=description)
    parser.add_argument("csv_path")
    return parser.parse_args()

def open_all_apps(csv_path):
    """Opens all apps listed in the CSV Path

    Args:
        csv_path (str): path to csv
    """
    
    print("Reading file: {}...".format(csv_path))
    with open(csv_path, mode="r") as file:
        print("Opening apps...")
        commands = util.convert_file_to_command_block(file)
        util.open_all_sites(commands)

def main():
    try:
        args = set_up_args()
        open_all_apps(args.csv_path)
        print("Program finished")
        
    except Exception as e:
        print("Oh my god its on fire {}\n".format(e))
        
if __name__ == "__main__":
    main()