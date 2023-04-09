# работа с csv
import csv

# построчное чтение csv через reader
# with open("files/newsafr.csv", encoding='utf-8') as f:
# 	reader = csv.reader(f)
# 	count = 0
# 	for row in reader:
# 		if row[-1] == 'title': # убрал заголовок
# 			continue
# 		print(row[-1])
# 		count += 1

# print(f"В этом файле {count} новостей")
# print()

# sys.exit()
 
# "utf-8" - unicode
# "cp1251" - Windows1251
# "koi8-r"

# чтение файла csv целиком. Не использовать для очень больших файлов!
# with open("files/newsafr.csv", encoding='utf-8') as f:
# 	reader = csv.reader(f)
# 	news_list = list(csv.reader(f))

# header = news_list.pop(0)

# for news in news_list:
# 	print(news[-1])
# print(f"В этом файле {len(news_list)} новостей")
# print()

# построчное чтение csv через DictReader
# dict = {}
# with open("files/newsafr.csv", encoding='utf-8') as f:
# 	reader = csv.DictReader(f)
# 	count = 0
# 	for row in reader:
# 		print(row["title"])
# 		count += 1

# print(f"В этом файле {count} новостей")
# print()

# построчное чтение csv через DictReader в список словарей

# with open("files/newsafr.csv", encoding='utf-8') as f:
# 	new_dict = {}
# 	new_list2 = []
# 	reader = csv.DictReader(f)
# 	for item in reader:
# 		for key, val in item.items():
# 			# print(key)
# 			# print(val)
# 			new_dict[key] = val
# 		new_list2.append(new_dict)

# print(new_list2)
# print(f"В этом файле {len(new_list2)} новостей")
# print()


# exit()


# настройки чтения и записи csv - диалекты

# csv.register_dialect("csv_no_quote_comma", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
# csv.register_dialect("csv_quote_all_semicolon", delimiter=";", quoting=csv.QUOTE_ALL)

# print(header)
# print(news_list)
# print(type(header))

# запись файла csv (перезапись - "w", дозапись в конец - "a")
# with open("files/newsafr2.csv", "w", encoding='utf-8') as f:
# 	# writer = csv.writer(f, delimiter="	", quoting=csv.QUOTE_ALL, escapechar="\\" ) # quoting=csv.QUOTE_ALL quoting=csv.QUOTE_MINIMAL quoting=csv.QUOTE_NONE
# 	writer = csv.writer(f, "csv_quote_all_semicolon")  # все настройки сохранены в диалект
# 	writer.writerow(news_list[3:6]) 


# writerows -> [[], [], []] нужно положить список списков
# writerow -> [] нужно положить список

# "hello" -> [["h"], ["e"], ["l"]]

# exit()

import sys

# работа с xml
import xml.etree.ElementTree as ET

# открытие файла
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.parse("files/newsafr.xml", parser)
# print(tree)

# как получить информацию о теге xml
# root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)

# как перемещаться по дереву (findall или find)
# news_list = root.findall("channel/item")
# print(len(news_list))
# for news in news_list:
# 	print(news.find("title").text)
# 	print(news.find("description").text)

# titles_list = root.findall("channel/item/title")
# descr_list = root.findall("channel/item/description")
# for title in titles_list:
# 	print(title.text)

# запись xml файла
# tree.write("files/newsafr2.xml")

# сравнение прохода по словарю и xml
# news_list = json_data["rss"]["channel"]["items"]
# news_list = root.findall("channel/item")

# exit()

# =======================
# работа с json
# import json

# with open("files/newsafr.json") as f:
# 	json_data = json.load(f)

# print(type(json_data))
# news_list = json_data["rss"]["channel"]["items"]
# print(type(news_list))

# for news in news_list:
# 	print(news["title"])
# print(f"В этом файле {len(news_list)} новостей")

# with open("files/newsafr2.json", "w") as f:
# 	json.dump(json_data, f, ensure_ascii=False, indent=4)

# with open("files/newsafr2.json") as f:
# 	json_data = json.load(f)
# 	json_text = json.dumps(json_data, ensure_ascii=False)

# print(json_text)

# exit()

# =======================
