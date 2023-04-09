from pprint import pprint

# сделаем словарь из файла рецепта

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip().replace('\ufeff', '') # Избавляюсь от BOM, не знаю откуда оно берется
        count_dishes = int(file.readline().strip())
        ingridients_list = []
        for _ in range(count_dishes):
            name, quant, pieces= file.readline().strip().split(' | ')
            ingridients_list.append({
                'ingredient_name': name,
                'quantity': int(quant),
                'measure': pieces
            })
        file.readline()
        cook_book[dishes_name] = ingridients_list

    # pprint(cook_book, sort_dicts=False)

print()
print('Проверяем полученный словарь из файла:')
print(cook_book)
print()

# сохраним словарь в файл, вдруг пригодится

with open('recipes_dict.txt', 'w', encoding='utf-8') as file:
    for key,val in cook_book.items():
        file.write('{}:{}\n'.format(key,val))

# функция для пересчета рецепта в соответствие с нужным количеством блюд (делаем список)

def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for d in dishes:
        for dd in cook_book.keys():
            if d == dd:
                for q in cook_book[dd]:
                    q['quantity'] *= person_count
                    dishes_dict[q['ingredient_name']] = q
    # pprint(dishes_dict, sort_dicts=False)
    return dishes_dict

new_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print('Проверяем что возвращает функция по заданным параметрам:')
print(new_dict)
print()

# сохраним новый словарь в файл, вдруг пригодится

with open('dishes_dict.txt', 'w', encoding='utf-8') as file:
    for key,val in new_dict.items():
        file.write('{}:{}\n'.format(key,val))
        