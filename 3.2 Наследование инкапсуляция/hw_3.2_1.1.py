class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, lecturer_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [lecturer_grade]
            else:
                lecturer.lecturer_grades[course] = [lecturer_grade]
        else:
            return 'Ошибка'    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 

class Lecturer(Mentor):

    lecturer_grades = {}

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade): # по правильному этому методу лучше дать другое название, не как у оценки студентов лекторам? Хотя по приоритету сработает и так правильно.
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создаем объект класса "Лучший студент" и назначаем курсы, которые он изучает
best_student = Student('Mikhaylov', 'Viktor', 'M')
best_student.courses_in_progress += ['Python from zero'] # или лучше сразу указать все курсы? ['Python from zero', 'GIT', 'OOP'] 
best_student.courses_in_progress += ['OOP']
best_student.finished_courses += ['GIT']

print()
print(f' Словарь лучший студент, пока без оценок: {best_student.__dict__}')
print(f' Изучаемые курсы лучшим студентом: {best_student.courses_in_progress}')
print(f' Оконченные курсы лучшим студентом: {best_student.finished_courses}')
print(f' ФИО лучшего студента: {best_student.name} {best_student.surname}')
print()
 
# Создаем объект "Крутой проверяющий" и назначаем курсы, которые он проверяет
cool_reviewer = Reviewer('Dmitry', 'Kachalov')
cool_reviewer.courses_attached += ['GIT']
cool_reviewer.courses_attached += ['Python from zero']
cool_reviewer.rate_hw(best_student, 'GIT', 7) 
# оценка не добавится, так как курс студентом уже закончен, сработает проверка условия в методе rate_hw
cool_reviewer.rate_hw(best_student, 'Python from zero', 9)
cool_reviewer.rate_hw(best_student, 'Python from zero', 8)
 
print(f' Словарь крутой проверяющий: {cool_reviewer.__dict__}')
print(f' Крутой проверяющий: {cool_reviewer.name} {cool_reviewer.surname}')
print(f' Оценки от проверяющего лучшему студенту: {best_student.grades}')
print()

# Создаем объект "Крутой лектор" и назначаем курсы, которые он преподает, выставляем ему оценки
cool_lecturer = Lecturer('Oleg', 'bulygin')
cool_lecturer.courses_attached += ['OOP','Python from zero']
best_student.rate_hw(cool_lecturer, 'OOP', 10)
best_student.rate_hw(cool_lecturer, 'GIT', 10) 
# оценка не добавится, так как курс студентом уже закончен, и лектор его не преподает, сработает проверка первого из этих двух условий
best_student.rate_hw(cool_lecturer, 'Python from zero', 9)
best_student.rate_hw(cool_lecturer, 'Python from zero', 10)

print(f' Словарь крутой лектор: {cool_lecturer.__dict__}')
print(f' Оценки крутому лектору от лучшего студента: {cool_lecturer.lecturer_grades}')
print()

print(f' Словарь лучшего студента с оценками: {best_student.__dict__}')
print()