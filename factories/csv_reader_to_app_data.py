from data.AppData import AppData

class CSV_Reader_To_App_Data:
    
    def __init__(self):
        pass
    
    @staticmethod
    def convert(csv_reader_output: list[str]):
        path = csv_reader_output[0]
        urls = []
        for i in range(1, len(csv_reader_output) - 1):
            url = csv_reader_output[i]
            if (url == '' or url == None):
                continue
            urls.append(csv_reader_output[i])
        return AppData(path, urls)  