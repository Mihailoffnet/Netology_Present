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
   * python manage.py runserver 0.0.0.0:8000 - проверяем, запускаем сервер с указанием ip 0.0.0.0:8000 для запуска из под виртуального сервера
   * 151.248.122.14:8000 - запускаем проект из браузера для проверки и видим ответ django

# Развертывание проекта 2
## Создаем виртуальный сервер и подключаемся к нему под своим логином (под root лучше не работать)
* ssh root@11.11.11.11 - подключаемся к серверу под root
* adduser mihailoff - создаем пользователя, указываем пароль
* usermod mihailoff -aG sudo - назначаем пользователя суперпользователем
* su mihailoff - переключаемся на пользователя
## Развертываем ПО на сервере
* sudo apt update - обновляем список доступных пакетов
* sudo apt upgrade - обновляем пакеты

* sudo apt install python3-venv python3-pip postgresql nginx - устанавливаем пакетно venv и pip для пайтона, postgres и nginx
* sudo systemctl status postgresql - проверяем, что постгрес запущен (Active)
* sudo systemctl restart postgresql - Если не запущен (not Active), то перезапускаем
* sudo systemctl start postgresql - или запускаем
* sudo systemctl start nginx - запускаем nginx
* sudo systemctl status nginx - проверяем, что nginx запущен (Active)
* sudo systemctl restart nginx - Если не запущен (not Active), то перезапускаем
* sudo systemctl start nginx - или запускаем
* можно проверить, что nginx запущен в браузеер по ip сервера в браузере (видим приветствие nginx)
* python3 --version - проверяем, есть ли пайтон и какой он версии
* git --version - проверяем, есть ли гит и какой он версии  
в ubuntu по умолчанию пайтон и гит уже установлены
пайтон в убунту вызывается командой python3

## Скачать проект django
* копируем ссылку на репозиторий с джанго в code https github https://github.com/Mihailoffnet/ForHomeWork.git
* git clone https://github.com/Mihailoffnet/ForHomeWork.git - копируем папку из репозитория к себе на сервер
* git checkout branch - переключаемся на нужную ветку при необходимости
* сd /ForHomeWork/6\ Django/6.6\ CRUD\ DRF/patch - переходим в нужную папку с файлом manage.py
* python3 -m venv env - создаем виртуальное окружение env
* source env/bin/activate - активируем созданное виртуальное окружение (видим имя виртуального окружение в пути в терминале)
* which python - можно проверить что виртуальное окружение активно. Покажет путь от папки с вирт. окружением
* pip install -r requirements.txt - устанавливаем нужные модули из файла requirements.txt
* pip freeze - проверяем что в виртуальном окружении только нужные нам пакеты (значит все работает как надо)

* pip install gunicorn - устанавливаем gunicorn (стандартный WSGI сервер для python)

## Создаем и настраиваем БД
* sudo su postgres - переключаемся на пользователя постгрес
* psql - входим в psql
* ALTER USER postgres WITH PASSWORD 'postgres'; - устанавливаем пароль для пользователя postgres
* CREATE DATABASE my_db; - создаем базу данных
* \q - выход из psql
* exit - выходим из под пользователя postgres

### Лучше использовать переменные из переменного окружения, чтобы не светить пароли
* pip install python-dotenv - устанавливаем библиотеку для работы с переменными
* nano .env создать файл для переменных и записать туда данные  
например
```
# django settings.py
DJANGO_SECRET_KEY=django-insecure-nw^y+m^wmxza1asgk+)!ua2qx9)g+#v=6%76-9i8i(6eqiw94j
DJANGO_DEBAG=True
DJANGO_ALLOWED_HOSTS=11.11.11.11
DB_ENGINE=django.db.backends.postgresql
DB_NAME=my_db
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
```
* ctrl+o сохраняем и ctrl+x выходим из редактора
* nano path/settings.py - Редактируем файл сеттингс джанго, прописываем переменные из виртуального окружения
```
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBAG = os.getenv('DJANGO_DEBAG')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')

ENGINE = os.getenv('DB_ENGINE')
NAME = os.getenv('DB_NAME')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
```
* python manage.py migrate - применяем миграции. Если применились значит все ок.
* python manage.py runserver 0.0.0.0:8000 - проверяем, запускаем сервер с указанием ip 0.0.0.0:8000 для запуска из под виртуального сервера
* 11.11.11.11:8000 - запускаем проект из браузера для проверки и видим ответ django
* ctrl+c - останавливаем сервер

## Запустим gunicorn и проверим работу нашего проекта не из под джанго
* ls stocks_products/ - ищем файл wsgi.py в папке с приложением джанго, к которому будет подключаться gunicorn
* gunicorn stocks_products.wsgi -b 0.0.0.0:8000 - запускаем сервер через gunicorn
* 11.11.11.11:8000 - проверяем в браузере, что проект запустился (но без библиотеки стилей, без статики)
* ctrl+c - останавливаем сервер

## Настраиваем проект
в файле wsgi.py есть переменная application, которая определяет настройки джанго (точка входа в джанго проект). Менять в этом файле ничего не нужно
### Нам нужно создать в операционной системе процесс DEMON, который будет постоянно работать и сам запускать наш проект на сервере
* Sudo nano /etc/systemd/system/gunicorn.service - создаем файл запуска в операционной системе
```
[Unit] #справочный раздел с описанием сервиса. 
Descriptions=Gunicorn service # Просто текст. Можно написать что угодно
After=network.target # переменная с указанием,когда нужно запускать процесс. После запуска сети

[Service] # Описываем как сервис gunicorn будет работать, что будет делать
User=mihailoff # Указываем своего пользователя
Group=www-data # Указываем группу
WorkingDirectory=/home/mihailoff/patch # Указываем путь до нашего виртуального окружения, корневую папку нашего проекта (папка с manage.py) это и есть полный путь до нашего виртуального окружения
ExecStart=/home/mihailoff/patch/env/bin/gunicorn  stocks_products.wsgi:application --workers=3 -b unix:/home/mihailoff/patch/stocks_products/project.sock
# Указываем, какой командой будет запускаться проект (путь к Файлу gunicorn в виртуальном окружении, путь к файлу wsgi нашего проекта, количество воркеров из расчета 2-3 на 1 ядро сервера, задаем создание сокета project.sock там же где файл wsgi. Название любое расширение .sock)

[Install]
WantedBy=multi-user.target # В каком режиме будет работать процесс. Ожидание - много пользователей
```
* ctrl+o, ctrl+x - сохраняем и закрываем файл
* sudo systemctl start unicorn - запускаем процесс (указываем название файла gunicorn.service)
* sudo systemctl enable unicorn - прописываем автозапуск unicorn, процесс будет автоматически перезапускаться в случае перезагрузки операционной системы
* sudo systemctl status unicorn - проверим, что статус Active

### К процессу unicorn подсоединяем наш веб-сервер
Для того, что бы веб-сервер смог общаться с джанго через гуникорн, мы должны его настроить
* sudo nano /etc/nginx/sites-available/project- Создаем конфигурационный файл project (название файла любое, обычно по названию своего проекта) И указываем внутри директиву для сервера:
   * слушать порт 80 
   * имя сервера это либо ip адрес либо доменное имя
   * указываем как искать пути
      * пути к статик файлам (ваша папка проекта с файлом manage.py). По указанному пути unicorn будет искать папку static
      * пути к остальным запросам перенаправляем на сокет в gunicorn

```
server {
   listen 80;
   server_name 11.11.11.11;

   location /static/ {
      root /home/mihailoff/patch;
   }
   location / {
      include proxy_params;
      proxy_pass http://unix:/home/mihailoff/patch/stocks_products/project.sock;
   }
}
```
* ctrl+o, ctrl+x - сохраняем и закрываем файл

Для применения настроек делаем два (в редких случаях три) шага
* sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled/ - создаем ссылку на файл иперводим его статус в запущенный
* sudo systemctl restart nginx (или nginx -s reload) - перезапускаем nginx
* sudo systemctl status nginx - проверяем, что nginx запущен (Active)
* 11.11.11.11 - проверяем сайт в браузере без указания порта
Может быть два варианта (порлучаем страницу джанго без стилей или получаем 502 ошибку)
Если получили 502 ошибку, то выполняем:
* sudo nano /etc/nginx/nginx.conf - открываем общие настройки nginx
в первой строчке меняем user www-data на своего пользователя mihailoff
```
user mihailoff;
```
* ctrl+o, ctrl+x - сохраняем и закрываем файл
* sudo systemctl restart nginx - перезапускаем nginx
* sudo systemctl status nginx - проверяем, что nginx запущен (Active)
* 11.11.11.11 - перепроверяем сайт в браузере (будет без стилей, без статики)

При необходимости перезапустить gunicorn необходимо перезапустить daemon
* sudo systemctl restart gunicorn - перезапускаем гуникорн и видим, что необходимо перезапустить daemon-reload
* sudo systemctl daemon-reload - перезапускаем daemon-reload
* sudo systemctl restart gunicorn - проверяем что статус gunicorn - Active

### Копируем статику в папку static проектаб которую мы ранее указали в настройках
Добавим django.contrib.staticfiles в INSTALLED_APPS (проверяем, что оно есть), укажем STATIC_URL и собираем статику в STATIC_ROOT в settings.py
* nano stocs_products/settings.py
```
DEBUG = True
INSTALLED_APPS = [
...
'django.contrib.staticfiles',
...
]
...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
* ctrl+o, ctrl+x - сохраняем и закрываем файл
* python manage.py collectstatic - копируем статику в нужную папку
получаем статус: 168 static files copied to '.../static'
* ls static/ - проверяем, что в папке статик появились подпапки
* 11.11.11.11 - проверяем в браузере, что теперь джанго отображается со стилями
Готово



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


