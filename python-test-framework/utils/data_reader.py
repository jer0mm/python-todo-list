import json

class DataReader:
    def read_user_data(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
