from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, reverse
from datetime import datetime
from app.models import Car, Person
import os
import random

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        # 'Админка': reverse('admin'),
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Показать приветствие из шаблона': reverse('hello'),
        'Показать приветствие с параметрами name и age': reverse('hello_name'),
        'Тестируем пагинацию': reverse('pagi'),
        'Создать машину': reverse('newcar'),
        'Посмотреть машины': reverse('cars'),
        'Создать владельцев для всех авто': reverse('newperson'),
        'Посмотреть владельцев машин': reverse('people'),
        # 'Показать сумму параметров /a/b/': reverse('sum')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%d:%m:%Y %H:%M:%S - %A')
    msg = f'<b>Текущее время: {current_time}</b>'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории

    listdir = (os.listdir())
    msg = ''
    for d in listdir:
        msg += f'- {d}<br>'
    return HttpResponse(f'<b>{msg}</b>')
    # raise NotImplemented

def hello_view(request):
    context = {
        'test': 5,
        'data': [1, 5, 8],
        'val': 'Hello',
    }
    return render(request, 'demo.html', context)

def hello_name(request):
    name = request.GET.get('name', 'anonimus')
    age = int(request.GET.get('age', '99'))
    return HttpResponse(f'<b>Hello, {name}, тебе уже {age}</b>')

def sum_view(request, a=0, b=0):
    result= a + b
    return HttpResponse(f'Сумма равно: {result}')

CONTENT = [str(i) for i in range(10000)]

def pagi_view(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)

def create_car(request):
    brand = request.GET.get('brand', random.choice(['Mercedes', 'BMV', 'WV']))
    model = request.GET.get('model', random.choice(['GLK', 'X3', 'Tuareg']))
    color = request.GET.get('color', random.choice(['black', 'green', 'blue']))
    car = Car(brand=brand, model=model, color=color)
    car.save()
    return HttpResponse(f'Создана машина: {car.brand}, {car.model}')

def list_car(request):
    brand = request.GET.get('brand', '')
    # model = request.GET.get('model', '')
    # color = request.GET.get('color', '')
    # car_objects = Car.objects.all()
    if brand:
        # car_objects = Car.objects.filter(brand=brand) # вызывать только выбранные данные
        # car_objects = Car.objects.filter(brand__contains=brand) # вызывать только данные, содержащие указанное вхождение
        car_objects = Car.objects.filter(brand__startswith=brand)  # вызывать только данные, начинающиеся с
    else:
        car_objects = Car.objects.all() # вызывать все данные из базы, даже те что не нужны
    cars=[f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    msg = ''
    for car in cars:
        person = Person(name="anonimus", car=car)
        person.save()
        # или второй вариант
        Person.objects.create(name="anonimus", car=car)
        msg += f'Создан владелец {person.name} автомобиля {car.brand}, {car.model} - {car.color}<br>'
    return HttpResponse(f'<b>Созданы владельцы для всех авто:</b> <br> {msg}')

def list_person(request):

    person_objects = Person.objects.all()
    people=[f'{p.id}: {p.name} с автомобилем {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))