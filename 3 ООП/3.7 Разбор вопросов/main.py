import pandas as pd
import requests
from bs4 import BeautifulSoup # библиотека для парсинга



def get_netology_posts():
    res = requests.get('https://netology.ru/blog/')
    soup = BeautifulSoup(res.text)
    news = soup.find_all('div', 'posts__item')
    netology_blog = pd.DataFrame()

    for article in news:
        title = article.find('a', 'posts__link').text
        # print(title)
        link = article.find('a', 'posts__link').get('href')
        # print(link)
        date = article.find('div', 'posts__date').text
        # print(date)
        category = article.find('a', 'tags__item').text
        # print(category)
        row = {'date': date, 'title': title, 'link': link, 'category': category}
        netology_blog = pd.concat([netology_blog, pd.DataFrame([row])])
    
    return netology_blog.reset_index(drop=True)

# res = get_netology_posts()


# print(res['title']) # вывод всех заголовков
# print(res.iloc[1:5, 3]) # вывод новостей 2-5 только третий столбец
# print(res[res['title'].str.contains('Python')]) # вывод новости по слову в заголовке
# print(res[res['title'].str.contains('ChatGPT')]) # вывод новости по слову в заголовке

# парсинг статей по поиску по ключам

def get_posts_by_search(queries):
    url = 'https://netology.ru/blog/'
    netology_blog = pd.DataFrame()

    for q in queries:
        params = {'s': q}
        res = requests.get(url, params)
        # print(res)
        soup = BeautifulSoup(res.text)
        articles = soup.find_all('article', 'status-publish')
        for article in articles:
            title = article.find('h2', 'entry-title').text
            link = article.find('h2', 'entry-title').find('a').get('href')
            date = article.find('span', 'posted-on').text.strip() # strip() убирает разрыв строк /n
            if article.find('div', 'entry-cats'): # Не во всех статьях есть категория. 
                category = article.find('div', 'entry-cats').text
            else:
                category = 'Новость' # Где категории нет - это новости, присваиваем категорию новости
            row = {'date': date, 'title': title, 'link': link, 'category': category}
            netology_blog = pd.concat([netology_blog, pd.DataFrame([row])])

    return netology_blog.reset_index(drop=True) 

# print(get_posts_by_search(['python', 'data science']))

import nltk # библиотека для работы с текстами



