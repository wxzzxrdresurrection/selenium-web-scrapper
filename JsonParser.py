import json

class JsonParser:

    def __init__(self, json_file):
        self.json_file = json_file
        self.config_data = self.load_file()
    
    def load_file(self):
        with open(self.json_file, 'r') as file:
            return json.load(file)
        
    def get_config(self):
        return self.config_data