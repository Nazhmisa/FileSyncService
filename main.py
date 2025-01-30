import os
import time
import configparser
import logging
from cloud_storage import CloudStorage

config = configparser.ConfigParser()
config.read("config.ini")

local_folder = config["Settings"]["local_folder"]
cloud_folder = config["Settings"]["cloud_folder"]
sync_interval = int(config["Settings"]["sync_interval"])
log_file = config["Logging"]["log_file"]
token = config["Settings"]["token"]

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Сервис синхронизации запущен.")


def sync_files():
    cloud = CloudStorage(token, cloud_folder)

    while True:
        try:
            local_files = set(os.listdir(local_folder))
            cloud_files = cloud.get_info()

            print(f"Локальные файлы: {local_files}")
            print(f"Файлы в облаке: {cloud_files}")

            for file in local_files - cloud_files:
                cloud.upload(os.path.join(local_folder, file))
                logging.info(f"Загружаем новый файл: {file}")

            for file in local_files & cloud_files:
                cloud.reload(os.path.join(local_folder, file))
                logging.info(f"Обновлен файл: {file}")

            for file in cloud_files - local_files:
                cloud.delete(file)
                logging.info(f"Удален файл: {file}")

        except Exception as e:
            logging.error(f"Ошибка при синхронизации: {str(e)}")

        time.sleep(sync_interval)
