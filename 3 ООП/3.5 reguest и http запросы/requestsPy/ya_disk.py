from pprint import pprint

import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        # pprint(f'json из гет файлс лист {response.json()} {type(response.json)}')
        # pprint(f'контект из гет файлс лист {response.content}')
        print(response.status_code)
        # print() 
        return response.json()
    
    # запрашиваем ссылку для загрузки

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 409:
            pprint(response.status_code)
            print(f'Пути {disk_file_path} не существует. Работа программы остановлена')
            exit()
        return response.json()

    def upload_file_to_disk (self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path)
        url = href.get('href')
        # print(f'ссылка для загрузки файла {url}')
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        # print(response.status_code)
        if response.status_code == 201:
            print("Success")

    def _great_folder(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": file_path}
        response = requests.put(url=url, headers=headers, params=params)
        print(response.status_code)
        return response
