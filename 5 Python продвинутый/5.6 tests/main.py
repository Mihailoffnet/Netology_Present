def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


def get_list():
    return [1, 2, 3, 4]

# a = ['Milk', 'Eggs', 'Milk', 'Meat', 'Bread', 'Milk', 'Spam', 'Butter', 'Sugar']
def get_most_popular(items: list) -> str:
    list_ = []
    for i in set(items):
        list_.append([i, items.count(i)])
    list_.sort(key=lambda x:x[1], reverse=1)
    return list_[0]


# res = get_most_popular(a)
#
# print(res)

# a = 10
# b = 2
# expected = 12
# result = summarize(a, b)
# assert result == expected
#
# a = 10
# b = 20
# some_num = 100
# result = multiply(a, b)
# assert result > some_num

# ==, !=, >, <, >=, <=
# is, is not
# in, not in
# is None, is not None
# isinstance()

# range1 = range(100, 200)
# result = summarize(56, 42)
# assert result in range1

SOME_NUMBER = 40
