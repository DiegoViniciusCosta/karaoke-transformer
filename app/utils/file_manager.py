
import os
import json

class FileManager:
    def save_json(self, file_name, data, folder):
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"{file_name}.json")
        with open(file_path, "w") as f:
            json.dump(data, f)
        return file_path
