# https://replit.com/@obulygin/LivelyDarkturquoiseLine#main.py
# def square(number):
#   '''
#   Возведение числа в квадрат
#   '''
#   result = number ** 2   
#   return result

# a = square(6)
# print(a)

# help(square)

# # функция с запросом данных
# def square_2():
#     user_input = float(input('Введите число'))
#     return user_input ** 2

# # print(square_2())

# # можно задать значение по умолчанию
# def power(number, number_2=2):
#     result = number ** number_2
#     return result


# print(power(4, 3)) # 64
# print(power(4)) # 16


# # функция без return
# def square_3(number):
#     result = number ** 2
#     print(result)
#     # return

# # print(square_3(6))

# res = square_3(6)

# print(res) # выдаст принт из функции и None из этой строки

# # локальные и глобальные переменные
# salary = 1000
# bonus = 300

# def info():
#     print(salary + bonus)

# # info()

# def info_2():
#     bonus = 200
#     print(salary + bonus)

# info_2()

# # глобальные переменные из локальных функций

# bonus = 300

# def info_3():
#     salary = 700
#     global bonus
#     bonus = 200
#     global some_number
#     some_number = 1
#     print(salary + bonus)

# print(bonus)
# info_3()
# print(bonus)

# print(some_number)

# # лямбда функции - короткая функции в одну строку, не объявляется через def и может не иметь имени

# lambda x, y: x - y
# print((lambda x, y: x - y)(5, 7)) # -2

# my_func = lambda x, y: x - y
# print(my_func(7, 10)) #-3

# print(list(map(lambda number: number**2, [5, 6, 7, 8, 8, 9]))) # применяет функцию к каждому объекту из списка

# Работа со списком студентов
students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 7, 9], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10], "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 8, 8, 9, 8],"exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
]

# найдем средний балл за экзамен по всей группе
def get_avg_exam_grade(students):
    sum_ex = 0
    for student in students:
        sum_ex += student['exam']
    return round(sum_ex / len(students), 2)

print(f'средний балл за экзамен по всей группе {get_avg_exam_grade(students_list)}')
print()

# найдем средний балл по всей группе
def get_avg_hw_grade(students):
    sum_hw = 0
    for student in students:
        sum_hw += sum(student['grade']) / len(student['grade'])
    return round(sum_hw / len(students), 2)

print(f'средний балл по всей группе {get_avg_hw_grade(students_list)}')
print()

# найдем баллы выше среднего за экзамен
def get_best_students(students):
    avg_grade = get_avg_exam_grade(students)
    for student in students:
        if student['exam'] >= avg_grade:
            print(f'{student["name"]} {student["surname"]} с баллом {student["exam"]}')
print('Студенты с баллом выше среднего:')
get_best_students(students_list)
print()

# найдем средний балл по всей группе и по полу
def get_avg_hw_grade(students, gender=None):
    sum_hw = 0
    counter = 0
    for student in students:
        if student['gender'] == gender or gender is None:
            sum_hw += sum(student['grade']) / len(student['grade'])
            counter += 1
    return round(sum_hw / counter, 2)

print('средний балл у всех студентов',get_avg_hw_grade(students_list))
print('средний балл у мальчиков', get_avg_hw_grade(students_list, 'м'))
print('средний балл у девочек',get_avg_hw_grade(students_list, 'ж'))
print()

# программа для вывода всех предыдущих функций
def main(students):
    print('Доступные команды: 1, 2, 3 или q')
    print()
    while True:
        comand = input('Введите команду ')
        if comand == '1':
          print(f'средний балл по всей группе {get_avg_hw_grade(students_list)}')
          print()
        elif comand == '2':
          print('средний балл у всех студентов',get_avg_hw_grade(students_list))
          print('средний балл у мальчиков', get_avg_hw_grade(students_list, 'м'))
          print('средний балл у девочек',get_avg_hw_grade(students_list, 'ж'))
          print()
        elif comand == '3':
          print('Студенты с баллом выше среднего:')
          get_best_students(students)
          print()
        elif comand == 'q':
          print('Выход')
          break

main(students_list)