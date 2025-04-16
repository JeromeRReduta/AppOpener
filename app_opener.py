from pywinauto.application import Application
import csv
from factories.csv_reader_to_app_data import CSV_Reader_To_App_Data
from argparse import ArgumentParser

description = """An app that opens up a list of files in a CSV, alongside any URLS.

                 For example, this app can open several Chrome tabs at given links."""

def get_csv_path():

    parser = ArgumentParser(description=description)
    parser.add_argument("csv_path")
    return parser.parse_args().csv_path

class AppOpener:
        
    def __init__(self, file):        
        values = csv.reader(file) 
        next(values, None) # skips headers
        self.__data_set = {CSV_Reader_To_App_Data.convert(row) for row in values}
            
    def openAll(self):
        for data in self.__data_set:
            for arg in data.urls:
                Application(backend="uia").start(r'{} "{}'.format(data.path, arg))

def main():
    try:
        csv_path = get_csv_path()
        print("Reading file: {}...".format(csv_path))
        with open(csv_path, mode='r') as file:
            print("Opening apps...")
            AppOpener(file).openAll()
        print("Done!")
        
    except Exception as e:
        print("Oh my god its on fire {}\n".format(e))
        
if __name__ == "__main__":
    main()