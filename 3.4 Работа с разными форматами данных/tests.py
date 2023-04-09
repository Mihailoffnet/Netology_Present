import json

with open("har_file.json") as f:
	json_data = json.load(f)

print(type(json_data))
news_list = json_data["log"]["entries"]["response"]["content"]
print(type(news_list))