"""
<h2 class="tm-title tm-title_h2"><a href="/ru/articles/745916/" class="tm-title__link" data-test-id="article-snippet-title-link" data-article-link="true"><span>Solidity: Путешествие в сердце оптимизации</span></a></h2>
"""
"""
<time datetime="2023-07-04T15:58:52.000Z" title="2023-07-04, 18:58">1 час назад</time>
"""

"""
div id="post-content-body"
"""

import bs4
import fake_headers
import requests

headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

response = requests.get("https://habr.com/ru/all/", headers=headers_dict)
main_html_data = response.text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")

articles_tag = main_html.find("div", class_="tm-article-list")

articles_tags = main_html.find_all("article")

parsed_data = []

for article_tag in articles_tags:
    h2_tag = article_tag.find("h2")
    a_tag = h2_tag.find("a")
    span_tag = a_tag.find("span")
    time_tag = article_tag.find("time")

    link = f"https://habr.com{a_tag['href']}"
    title = span_tag.text
    date_time = time_tag["datetime"]

    response = requests.get(link, headers=headers.generate()).text
    article_html = bs4.BeautifulSoup(response, "lxml")
    article_full_tag = article_html.find("div", id="post-content-body")
    article_full_text = article_full_tag.text[100]

    parsed_data.append(
        {
            "title": title,
            "link": link,
            "date_time": date_time,
            "text": article_full_text,
        }
    )

print(parsed_data)
