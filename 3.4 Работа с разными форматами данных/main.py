# https://replit.com/@shorstko/netologyfileformats230403#main.py

import sys

import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("files/newsafr.xml", parser)
print(tree)

root = tree.getroot()
print(root.tag)
print(root.attrib)
print(root.text)

news_list = root.findall("channel/item")
print(len(news_list))
for news in news_list:
	print(news.find("title").text)
	print(news.find("description").text)

titles_list = root.findall("channel/item/title")
descr_list = root.findall("channel/item/description")
for title in titles_list:
	print(title.text)

tree.write("files/newsafr2.xml")

# сравнение прохода по словарю и xml
# news_list = json_data["rss"]["channel"]["items"]
# news_list = root.findall("channel/item")

sys.exit()

import json

with open("files/newsafr.json") as f:
	json_data = json.load(f)

print(type(json_data))
news_list = json_data["rss"]["channel"]["items"]
print(type(news_list))

for news in news_list:
	print(news["title"])
print(f"В этом файле {len(news_list)} новостей")

with open("files/newsafr2.json", "w") as f:
	json.dump(json_data, f, ensure_ascii=False, indent=4)

# with open("files/newsafr2.json") as f:
# 	json_data = json.load(f)
# 	json_text = json.dumps(json_data, ensure_ascii=False)

# print(json_text)

sys.exit()

import csv

# with open("files/newsafr.csv") as f:
# 	reader = csv.reader(f)
# 	count = 0
# 	for row in reader:
# 		print(row[-1])
# 		count += 1

# print(f"В этом файле {count-1} новостей")

# "utf-8" - unicode
# "cp1251" - Windows1251
# "koi8-r"

with open("files/newsafr.csv") as f:
	reader = csv.reader(f)
	news_list = list(reader)

header = news_list.pop(0)

# for news in news_list:
# 	print(news[-1])
# print(f"В этом файле {len(news_list)} новостей")

# with open("files/newsafr.csv") as f:
# 	reader = csv.DictReader(f)
# 	count = 0
# 	for row in reader:
# 		print(row["title"])
# 		count += 1

# print(f"В этом файле {count} новостей")

csv.register_dialect("csv_no_quote_comma", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
csv.register_dialect("csv_quote_all_semicolon", delimiter=";", quoting=csv.QUOTE_ALL)

print(header)
print(type(header))

with open("files/newsafr2.csv", "w") as f:
	writer = csv.writer(f, "csv_quote_all_semicolon")
	writer.writerow(header)
	writer.writerows(news_list[3:6])

# writerows -> [[], [], []]
# writerow -> []

# "hello" -> [["h"], ["e"], ["l"]]