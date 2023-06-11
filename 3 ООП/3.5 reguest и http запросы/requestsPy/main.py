from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = "y0_AgAAAAAAUzO7AADLWwAAAADgU2u6YHDfksgdT-SrIGZJI_yRlvjFopA"

# =========================================
# # тестовый запрос

# def test_request():
#     my_url = "https://httpbin.org/get"
#     my_params = {"model": "nike123"}
#     my_headers = {"Authorization": "secret - token - 123"}
#     response = requests.get(url=my_url, params=my_params, headers=my_headers, timeout=5)
    
#     pprint(response.url) # посмотреть ссылку запроса
#     pprint(response.status_code) # статус ответа

#     # можно добавить проверкеу по статусу запроса

#     if response.status_code != 200: 
#         print('request error')
#     else:
#         print('good request')

#     # какие еще варианты получения ответа:
#     pprint(response.headers) # заголовки ответа
#     pprint(type(response.headers)) # класс requests.structures.CaseInsensitiveDict
#     pprint(response.content) # контент если есть
#     print(type(response.content)) # класс bytes
#     pprint(response.text) # ответ в виде текста
#     print(type(response.text)) # класс str
#     pprint(response.json()) # словарь json
#     print(type(response.json())) # класс dict

#     # обращаемся к словарю json по ключу 'headers' - и сразу обращаемся к словарю dyenhb значениz 'headers' по ключу 'User-Agent'

#     data = response.json()
#     user_agent = data.get('headers').get('User-Agent') 
#     print(user_agent) 
#     print(type(user_agent)) # класс str

# a = test_request() # запустить команду

# =========================================

if __name__ == '__main__':
    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())
    ya = YandexDisk(token=TOKEN)
    # получаем список файлов в виде словаря
    # data = ya.get_files_list()
    # pprint(data)
 
    a = ya.upload_file_to_disk('123/test.txt', 'test.txt')
    # # b = ya._great_folder('netology1')
    

    # # ya.upload_file_to_disk("test/netology", "test.txt")






