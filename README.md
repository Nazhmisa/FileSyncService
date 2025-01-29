# FileSyncService
Данный репозиторий создан для сдачи Практической Работы - "Сервис синхронизации файлов"

## Конфигурация

Сначала создал файл config.ini и вписал в него папку с которой будет производиться синхронизация и папку в облаке с которой будет синхронизирована локальная папка. Интервал синхронизации 60 секунд. А также вписал токен Яндекс.Диска из сайта:
```
https://yandex.ru/dev/disk/poligon#access_token=y0__xCMie3XARjblgMgmvnOkRI-h8SLlUKtZON045-CVK7RvkxLvQ&token_type=bearer&expires_in=31536000&cid=p24x3xrxj2dn2vf7e033p5nweg
```
Также ниже вписал файл логирования.

## Главный скрипт

Импортирую библиотеку os для работы с файлами и папками операционной системы. Библиотека time для установки задержки интервала синхронизации в 60 секунд. Библиотека configparser нужен для чтения настроек config.ini, а также logging для логирования и CloudStorage для работы с облаком.

Далее в основном скрипте прописываю настройки через переменную config в которую вложил значение configparser. Через config читаю настройки config.ini и присваиваю локальным переменным значения из файла config.ini.

Далее настраиваю логгирование синхронизации.

Добавил функцию sync_files() в которой несколько циклов проводят проверку на разницу между локальной папкой и облачной.

## Скрипт облачного хранилища

Импортировал библиотеку requests для запросов на сайт облачного хранилища

Создаю класс CloudStorage в конструкторе вношу атрибуты токена и папки

Создаю методы загрузки, обновления, удаления и логирования.