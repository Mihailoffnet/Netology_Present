# Работа с терминалом

## Пример конвейера

``` Картошка
котлеты
суп
Компот
Салат
Десерт
котлеты
Десерт
Компот
Салат
Компот
Десерт
Компот
котлеты
котлеты
Картошка
Компот
Салат
Картошка
Макароны
Тирамису
макароны 
```


$ cat test.txt | sed -e "s/\b\(.\)/\u\1/g" | sort | uniq -c | sort -r | cat > test2.txt

1. cat test.txt  читаем файл Test.txt
2. sed -e "s/\b\(.\)/\u\1/g" Делаем все первые символы заглавными
3. sort сортируем по имени
4.  uniq -c оставляем только уникальные значения и считаем их количество (параметр -c)
5. sort -r Сортируем по убыванию
6. cat > test2.txt записываем результат в файл
   
``` 5 Компот
4 Котлеты
3 Салат
3 Картошка
3 Десерт
2 Макароны
1 Тирамису
1 Суп 
```

# задать переменную команда export
* export PASSWORD=12345
* env - показать все переменные
* $ password=54321 python file2.py - переменная одноразовая для одной команды

## Создать и вызвать программу
* nano file1.py
* python  file1.py

## Пакет для использования множества переменных в пайтоне
* pip install python-dotenv
* nano .env создать файл для переменных и записать туда данные  
например
```
USER=postgres
PASSWORD='postgres'
DB_NAME=my_db
```

### Файл для запуска и использования переменных из .env должен их импортировать и загрузить
* from dotenv import load_dotenv
* load_dotenv
  
### Образец файла для запуска

```
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
db_name = os.getenv('DB_NAME')

DSN = f'postgresql://{user}:{password}@localhost:5432/{db_name}'

print(DSN)
```

## Пакеты - дополнительные программы, их можно устанавливать
в каждом терминале есть пакетный менеджер для установки дополнительных программ.  
В ubuntu это apt/snap (аналог pip в пайтоне)
Для установки используется команда
* apt install net-tools
Для установки от суперпользователя используется sudo  
* sudo apt install net-tools - установить пакет net-tools
* sudo apt remove net-tools - удалить пакет net-tools
* sudo apt update - обновить список доступных пакетов
* sudo apt upgrate - обновить сами пакеты

# Подключение к серверу

## Создаем SSH ключb (приватный rsa и публичный pub)
ssh-keygen
Подтверждаем место для ключа и указываем пароль по необходимости (можно без)
## ыводим на экран и копируем (добавляем) публичный ключ на сервер
cat ~/.ssh/id_rsa.pub

## подключиться к серверу по ip и паролю:
ssh root@151.248.122.14

### создать конфиг для более быстрого подключения:
touch ~/.ssh/config

### Редактируем содержимое конфига через nano ~/.ssh/config:
Host testserver
    HostName 151.248.122.14
    Port 22
    User root

### скопировать SSH на сервер для доступа без пароля
ssh-copy-id root@151.248.122.14

## подлкючиться без пароля по псевдониму из конфига
 ssh testserver

## Создаем юзера
* adduser mihailoff - создать юзера
* usermod mihailoff -aG sudo - добавляем пользователя в группу sudo (сеперюзер)
* su mihailoff - переключиться на нового юзера
* cd ~ - переходим в его домашнюю директорию

### Когда работаем от юзера (не от root) большинство команд нужно начинать с sudo

## Развертываем ПО на сервере (пайтон, гит, постгрес, venv, pip)
* sudo apt update - обновляем список доступных пакетов
* sudo apt upgrade - обновляем пакеты
* python3 --version - проверяем, есть ли пайтон и какой он версии
* git --version - проверяем, есть ли гит и какой он версии  
в ubuntu по умолчанию пайтон и гит уже установлены
пайтон в убунту вызывается командой python3
* sudo apt install postgresql - устанавливаем постгрес
* sudo systemctl status postgresql - проверяем, что постгрес запущен (Active)
* sudo systemctl restart postgresql - Если не запущен (not Active), то перезапускаем
* sudo systemctl start postgresql - или запускаем
* sudo apt install python3-venv python3-pip - устанавливаем пакетно venv и pip для пайтона

## Установка Django
1. Установить Python с виртауальным окружением (уже сделано)
   * sudo apt install python3-venv python3-pip
   * sudo apt install nginx - устанавливаем nginx
2. Установить Postgres (уже сделано) и создать БД (при необходимости)
   * sudo apt install postgresql - устанавливаем постгрес
   * sudo systemctl status postgresql - проверяем, что постгрес запущен (Active)
   * sudo systemctl restart postgresql - Если не запущен (not Active), то перезапускаем
   * sudo systemctl start postgresql - или запускаем
   *    
   * sudo su postgres - переключаемся на пользователя постгрес
   * psql - входим в psql
   * ALTER USER postgres WITH PASSWORD 'postgres' - устанавливаем пароль для пользователя постгрес
   * CREATE DATABASE my_db; - создаем базу данных
   * \q - выход из psql
   * exit - выходим из под пользователя постгрес
3. Скачать проект
   * копируем ссылку на репозиторий с джанго в code https github https://github.com/Mihailoffnet/ForHomeWork.git
   * git clone https://github.com/Mihailoffnet/ForHomeWork.git - копируем папку из репозитория к себе на сервер
   * git checkout branch - переключаемся на нужную ветку при необходимости
   * сd /ForHomeWork/6\ Django/6.6\ CRUD\ DRF/stocks_products - переходим в нужную папку с файлом manage.py
   * python3 -m venv my_env - создаем виртуальное окружение my_env
   * source my_env/bin/activate - активируем созданное виртуальное окружение (видим имя виртуального окружение в пути в терминале)
   * which python - можно проверить что виртуальное окружение активно. Покажет путь от папки с вирт. окружением
   * pip install -r requirements.txt - устанавливаем нужные модули из файла requirements.txt
   * pip freeze - проверяем что в виртуальном окружении только нужные нам пакеты (значит все работает как надо)
4. Внести корректировки в settings.py (при необходимости), но лучше при написании кода предусмотреть корректировку настроек через переменные окружения
   * nano stocks_products/settings.py - открываем редактолром нано файл настроек (указываем путь к файлу настроек)  
   * настраиваем подключение к БД
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'my_db',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
        }
    }
    ```
    * ctrl+o сохраняем и ctrl+x выходим из редактора
    * python manage.py migrate - применяем миграции. Если применились - значит все сделано правильно
    * 
5. Применить миграции
   * python manage.py migrate - применяем миграции. Если применились значит все ок.
6. Запустить сервер

# Развертывание проекта 2


# Ссылки
## Материалы по теме "Основы терминала":
* https://www.hostinger.com.ua/rukovodstva/osnovnyje-komandy-linux
* https://losst.ru/42-komandy-linux-kotorye-vy-dolzhny-znat
* https://www.youtube.com/playlist?list=PL7KBbsb4oaOnEdCxwKkRDXCUNZ-gPYf89

## туториалы:
* https://www.javatpoint.com/linux-tutorial
* https://ryanstutorials.net/linuxtutorial/
* https://ubuntu.com/tutorials/command-line-for-beginners#1-overview
* https://www.tutorialspoint.com/unix/index.htm

## клавиатурные сокращения терминала:
* https://habr.com/ru/post/663758/
* https://www.javatpoint.com/linux-terminal-shortcuts
* https://www.makeuseof.com/linux-bash-terminal-shortcuts/

## перенаправление потоков ввода-вывода:
* https://selectel.ru/blog/tutorials/linux-redirection/
* https://losst.ru/perenapravlenie-vvoda-vyvoda-linux
* https://andreyex.ru/linux/vvod-vyvod-i-perenapravlenie-oshibok-v-linux/
* https://serverspace.ru/support/help/standartnye-perenapravleniya-vvoda-vyvoda-v-linux/

## пакетный менеджер apt:
* https://ru.wikipedia.org/wiki/Advanced_Packaging_Tool
* https://losst.ru/kak-polzovatsya-apt
* https://help.ubuntu.ru/wiki/apt
* https://blog.sedicomm.com/2018/04/06/ispolzovanie-komand-apt-v-linux-polnoe-rukovodstvo/

## из материала лекции
* [Команды и их описание](https://www.opennet.ru/man.shtml)
* [про WSL/WSL2](https://docs.microsoft.com/ru-ru/windows/wsl/about)


