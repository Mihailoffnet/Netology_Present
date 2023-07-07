"""
<strong class="text-underline"><span class="table-ip4-home"> 128.0.240.238</span></strong>
"""
import bs4
import fake_headers
import requests

headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

response = requests.get("https://www.iplocation.net/", headers=headers_dict)
html_data = response.text
soup = bs4.BeautifulSoup(html_data, "lxml")
span_tag = soup.find("span", class_="table-ip4-home")
ip_address = span_tag.text
print(ip_address.strip())
