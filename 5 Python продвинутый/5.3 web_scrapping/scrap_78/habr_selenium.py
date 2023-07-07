from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint


def wait_element(driver, delay_seconds=1, by=By.TAG_NAME, value=None):
    """
    Иногда элементы на странце не прогружаются сразу
    Функция ждет delay_seconds если элемент еще не прогрузился
    Если за отведенное время элемент не прогружается выбрасывается TimeoutException
    :param driver: driver
    :param delay_seconds: максимальное время ожижания
    :param by: поле поиска
    :param value: значение поиска
    :return: найденный элемент
    """

    return WebDriverWait(driver, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://habr.com/ru/all/")

articles = driver.find_element(By.CLASS_NAME, "tm-articles-list")

parsed_data = []
for article in articles.find_elements(By.TAG_NAME, "article"):
    h2_element = article.find_element(By.TAG_NAME, "h2")
    a_element = h2_element.find_element(By.TAG_NAME, "a")
    span_element = a_element.find_element(By.TAG_NAME, "span")
    time_element = wait_element(driver, by=By.TAG_NAME, value="time")

    title = span_element.text
    link = a_element.get_attribute("href")
    date_time = time_element.get_attribute("datetime")

    parsed_data.append(
        {
            "title": title,
            "link": link,
            "date_time": date_time,
        }
    )

pprint(parsed_data)

for item in parsed_data:
    driver.get(item["link"])
    article = wait_element(driver, by=By.ID, value="post-content-body")
    item["text"] = article.text[:100]

pprint(parsed_data)