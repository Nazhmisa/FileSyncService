import os
import requests


class CloudStorage:
    def __init__(self, token, folder):
        self.token = token
        self.folder = folder

    def upload(self, path):
        filename = os.path.basename(path)
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": f"{self.folder}/{filename}", "overwrite": "true"}
        headers = {"Authorization": f"OAuth {self.token}"}

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            upload_url = response.json().get("href")

            with open(path, "rb") as file:
                requests.put(
                    upload_url,
                    data=file,
                    headers={"Authorization": f"OAuth {self.token}"},
                )
            print(f"Файл {filename} загружен в облако.")
        else:
            print(f"Ошибка при получении ссылки для загрузки: {response.text}")

    def reload(self, path):
        self.upload(path)

    def delete(self, filename):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": f"{self.folder}/{filename}", "permanently": "true"}
        headers = {"Authorization": f"OAuth {self.token}"}

        response = requests.delete(url, headers=headers, params=params)
        if response.status_code == 204:
            print(f"Файл {filename} удален.")
        else:
            print(f"Ошибка удаления файла {filename}: {response.text}")

    def get_info(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": self.folder}
        headers = {"Authorization": f"OAuth {self.token}"}

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            items = response.json().get("_embedded", {}).get("items", [])
            file_list = {item["name"] for item in items}
            print(f"Файлы в облаке: {file_list}")
            return file_list
        else:
            print(f"Ошибка при получении списка файлов: {response.text}")
            return set()
