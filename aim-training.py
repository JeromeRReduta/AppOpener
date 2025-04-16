from pywinauto.application import Application
import csv
from data.AppData import AppData
from factories.csv_reader_to_app_data import CSV_Reader_To_App_Data

csv_path = r"C:\Users\JRRed\OneDrive\aim-training-apps.csv"

'''
Opens the following:
* LG Hub (to check mouse battery)
* Spotify
* Chrome -> generic timer, Voltaic benchmarks, and VDIM page
* Excel -> Aim training notes 2025
* Steam -> Kovaak's Aim Trainer
'''

csv_path = r"C:\Users\JRRed\OneDrive\aim-training-apps.csv"
def main():
    try:
        my_file = open(csv_path, mode='r')
        parsed_data = csv.reader(my_file)
        next(parsed_data, None) # skips headers
        allAppData = [CSV_Reader_To_App_Data.convert(row) for row in parsed_data]
        for appData in allAppData:
            temp = [Application(backend="uia").start(r'{} "{}"'.format(appData.path, arg))
                for arg in appData.urls] # TODO: just make this a for loop, not list comp.
    except:
        print("Oh my god its on fire")
        
if __name__ == "__main__":
    main()