import requests

class CloudStorage:
    def __init__(self, token, folder):
        self.token = token
        self.folder = folder

    def upload(self, path):

        with open(path, "rb") as file:
            requests.post(f"https://disk.yandex.ru/client/disk/BackUpFolder={self.folder}", headers={"Authorization": f"Bearer {self.token}"}, files={"file": file})
    
    def reload(self, path):
        
        self.upload(path)
    
    def delete(self, filename):
        
        requests.delete(f"https://disk.yandex.ru/client/disk/BackUpFolder={self.folder}&file={filename}", headers={"Authorization": f"Bearer {self.token}"})
    
    def get_info(self):

        response = requests.get(f"https://disk.yandex.ru/client/disk/BackUpFolder={self.folder}", headers={"Authorization": f"Bearer {self.token}"})
        return set(response.json()["files"])