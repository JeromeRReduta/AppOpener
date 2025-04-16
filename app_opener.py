from pywinauto.application import Application
import csv
from factories.csv_reader_to_app_data import CSV_Reader_To_App_Data
from argparse import ArgumentParser
import app_openers as util

description = """An app that opens up a list of files in a CSV, alongside any URLS.

                 For example, this app can open several Chrome tabs at given links."""

def get_csv_path():

    parser = ArgumentParser(description=description)
    parser.add_argument("csv_path")
    return parser.parse_args().csv_path

def main():
    try:
        csv_path = util.get_csv_path()
        print("Reading file: {}...".format(csv_path))
        with open(csv_path, mode="r") as file:
            print("Opening apps...")
            commands = util.convert_file_to_commands(file)
            util.open_all_sites(commands)
            print("Program finished")
        
    except Exception as e:
        print("Oh my god its on fire {}\n".format(e))
        
if __name__ == "__main__":
    main()
    