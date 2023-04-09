import json


def read_json(file_path, word_max_len=6, top_words_amt=10):

    # откроем файл и прочитаем его в список словарей
	
	with open(file_path) as f:
		json_data = json.load(f)

	news_list = json_data['rss']['channel']['items'] # news_list type list


	# составим список из всех слов длинее 6 символов в новостях:

	word_list = []

	for item in news_list:
		item_list = item['description'].split(sep = ' ')
		for word in item_list:
			if len(word) > word_max_len:
				word_list.append(word)
	world_set = set(word_list)

	# составим словарь количество : слово
	word_dict = {}

	for s_word in world_set:
		count = word_list.count(s_word)
		if s_word in word_dict:
			print(f'дубль слово {s_word}')
			continue
		word_dict[s_word] = count
	word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:top_words_amt])
	# print(word_dict_sorted)

	# составим список из первых десяти элементов и выведем их на печать:

	topword_list =[]
	for topword in word_dict_sorted.keys():
		topword_list.append(topword)
	return topword_list

if __name__ == '__main__':
	print(read_json('newsafr.json'))


# import json

# # def read_json(file_path, word_max_len=6, top_words_amt=10):
# #       with open('newsafr.json') as f:
# #         json_data = json.load(f)
# #     news_list = json_data["rss"]["channel"]["items"]


# word_max_len=6
# top_words_amt=10
# file_path = 'newsafr.json'

# # откроем файл и прочитаем его в список словарей

# with open('newsafr.json') as f:
# 	json_data = json.load(f)

# news_list = json_data['rss']['channel']['items'] # news_list type list


# # составим список из всех слов длинее 6 символов в новостях:

# word_list = []

# for item in news_list:
# 	item_list = item['description'].split(sep = ' ')
# 	for word in item_list:
# 		if len(word) > word_max_len:
# 			word_list.append(word)
# # составим словарь количество : слово
# word_dict = {}

# for s_word in word_list:
# 	count = word_list.count(s_word)
# 	if s_word in word_dict:
# 		print(f'дубль слово {s_word}')
# 		continue
# 	word_dict[s_word] = count

# word_dict_sorted = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:top_words_amt])
# # print(word_dict_sorted)

# # составим список из первых десяти элементов и выведем их на печать:

# topword_list =[]
# for topword in word_dict_sorted.keys():
# 	topword_list.append(topword)

# print(topword_list)