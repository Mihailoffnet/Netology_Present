# загрузить postman https://www.postman.com/downloads/
# вики про UTM метки https://ru.wikipedia.org/wiki/UTM-%D0%BC%D0%B5%D1%82%D0%BA%D0%B8
# ответы (стутаусы) запросов https://http.cat/


from pprint import pprint

import requests

# from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = ""


def test_request():
    url = "https://bootssizes/get"
    params = {"model": "nike123"}
    headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url, params=params, headers=headers, timeout=5)
    pprint(response)


if __name__ == '__main__':
    reddit = Reddit()
    pprint(reddit.get_popular_videos())
    ya = YandexDisk(token="")
    ya.upload_file_to_disk("test/netology", "test.txt")