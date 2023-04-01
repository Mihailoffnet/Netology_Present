# чтение из файла

# прочтение файла как единой строки read()
# f = open('file1.txt', 'rt')
# f = open('file1.txt', 'r')
# f = open('file1.txt')

# content = f.read()
# print(content)
# print(type(content))
# f.close()

# построчное чтение readline()
# with open('file1.txt') as f:
#     result = f.readline()
#     result2 = f.readline()
#     print(result2)
#     print(type(result2))

# чтение файла в виде списка из строки readlines()
# with open('file1.txt') as f:
#     result = f.readlines()
#     # print(result)
#     print(type(result))
#     print(result[0:5])


#итерация по файлу
# with open('file1.txt') as f:
#     for line in f:
#         print(line)


#чтение из файла, который находится не в корне

#относительный путь (отсчитывается от текущего местоположения)
# with open('folder1/file2.txt') as file:
#     res = file.readline()
#     print(res)

#абсолютный путь (от корневой директории)
# with open(r'C:\Users\Адилет\Desktop\py_78_files\folder1\file2.txt') as f:
# import os
#
# current = os.getcwd()
# folder_name = 'folder1'
# file_name = 'file2.txt'
#
# # full_path = current + '\\' + folder_name + '\\' + file_name
#
# full_path = os.path.join(current, folder_name, file_name)
# print(full_path)

# with open(full_path) as f:
#     #\u, \t, \r, \n
#     res = f.readline()
#     print(res)

# os.listdir()

#запись в файл
#перезапись w
import os

lines = ['1\n', '2\n', '3\n', '4\n']

#запись по одной строке write()
# with open('file3', 'w') as file:
#     # file.write('Hello world!\n')
#     # file.write('Good evening!\n')
#     for l in lines:
#         file.write(l)

#запись нескольких строк writelines()
# with open('file3', 'w') as file:
#     file.writelines(lines)

#дозапись
# with open('file4', 'a') as file:
#     # file.write('How are you doing?\n')
#     file.writelines(lines)

#запись только в новый файл
# with open('file5', 'x') as f:
#     f.write('some data')
# os.remove('file4')

#ошибки

#несуществующий файл
# with open('some_data.txt') as f:
#     ...


#неверный режим
# with open('some_data.txt', 'w') as file:
#     file.read()


# режим x, когда файл существует
# f = open('file3', 'x')
# f.write('Hello!')


#записываемые данные не являются строкой
# f = open('file.txt', 'w')
# f.write(None)


#неверная кодировка
# str1 = 'Всем привет, дорогие друзья!'
# with open('hello.txt', 'w') as file:
#     file.write(str1)

# str1 = 'Всем привет, дорогие друзья!'
# with open('hello.txt', 'w', encoding='utf-8') as file:
#     file.write(str1)
#
# import requests
#
# URL = 'https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/maps-satellite-images/satellite-image-of-globe.jpg'
#
# response = requests.get(URL)
#
# with open('space.jpg', 'wb') as file:
#     file.write(response.content)

# {'HR': [{...}], 'IT': [...]}


from pprint import pprint

with open('data.txt', 'rt') as file:
    departments = {}
    for line in file:
        dep_name = line.strip()
        employees_count = int(file.readline().strip())
        employees = []
        for _ in range(employees_count):
            name, last_name, date, city = file.readline().strip().split(' | ')
            employees.append({
                'name': name,
                'last_name': last_name,
                'date_of_birth': date,
                'city': city
            })
        file.readline()
        departments[dep_name] = employees

    pprint(departments, sort_dicts=False)
