from functools import reduce

# print(reduce(lambda x, y: x*y, [1, 2, 3, 4, 5, 6]))


my_list = ['2018-01-01', 'yandex', 'cpc', 100]

print(reduce(lambda el_1, el_2: {el_2: el_1}, reversed(my_list)))