# CI/CD (сontinuous Integration/сontinuous delivery)

## Процесс внесения изменений на примере Django проекта

### Важно. При создании и настройке сервера необходимо помимо пайтона, постгрес и нгинкс установить пакет except
* sudo apt install except python3-venv python3-pip postgresql nginx 
  
1. Создать репозиторий в GitHub
   * Как правило у проекта, развернутого на сервере, уже есть репозиторий
2. Отправить в репозиторий измененный исходный код (с валидными тестами и линтерами)
   * git checkout -b master Создаем отдельную ветку master, при внесении изменений на которой будут происходить изменения на сервере
   * git add . добавляем измененные файлы в отслеживаемые
   * git commit -m "change..." - коммитим внесенные изменения 
   * git push origin master - отправляем изменения в гитхаб  
3. Залить изменения на сервер:  
   Что бы применить изменения на продакшен сервере, каждый раз нужно производить следующие манипуляции: 
    * ssh mihailoff@151.248.122.14 - подключаемся к серверу
    * cd patch/ - переходим в папку проекта
    * git pull origin master  - загружаем изменения
    * source env/bin/activate - активируем созданное виртуальное окружение (видим имя виртуального окружение в пути в терминале)
    * pip install -r requirements.txt - устанавливаем нужные модули из файла requirements.txt (если в изменениях появились новые модули)
    * python manage.py migrate - создаем миграции (если изменения влияют на бд)
    * sudo systemctl restart gunicorn - перезапускаем гуникорн
 
## Для автоматизации процессов автоматической заливки изменения на сервер, воспользуемся сервисом GitHub Actions  

1. Настраиваем GitHub Actions (добавляем виртуальные переменные):
   * Переходим в настройки GitHub репозитория проекта: Settings - Secret and variables - Actions
   * Нажимаем New repository secret и добавляем виртуальные переменные, используемые в проекте (и перечисленные в пункте 1 блок env:)
    ```
    Name* DJANGO_SECRET_KEY Secret* bwlgbj6gpqr325r0349t03ogj34rg345
    Name* DJANGO_DEBAG Secret* 0
    Name* DJANGO_ALLOWED_HOSTS Secret* localhost
    Name* DB_ENGINE Secret* django.db.backends.postgresql
    Name* DB_NAME Secret* my_db
    Name* DB_HOST Secret* 127.0.0.1
    Name* DB_PORT Secret* 5432  
    Name* DB_USER Secret* user_1
    Name* DB_PASSWORD Secret* 12345
    Name* SSH_HOST: Secret* 44.44.44.44 # ip сервера для подключения по SSH
    Name* SSH_USER: Secret* mihailoff # имя пользователя, от которого будет запускаться сриптs
    Name* SSH_PASSWORD: Secret* 12345 # пароль пользователя
    ```

GitHub Actions сканирует каталог .github/workflows на наличие скриптов в yml формате, соответствующих шаблону.

2. В корне нашего проекта создаем папку .github/workflows с файлом master.yml для написания сриптов (имя любое, взято по названию ветки)/
   * Пишем скрипт:
```
name: Автоматизация тестирования и развертывания проекта - задаем название для нашего скрипта

on: # блок команд on
    push: # отслеживаем действие, которое будет запускать исполнение срипта (push изменения на сервере)
        branches: [master] # указываем ветки, которые нужно отслеживать (в виде списка)

jobs: # блок команд jobs
    tests: # блок тестов, название модет быть любое
        runs-on: ubuntu-22.04 # указываем ОС, на которой будут происходить тесты (та же ОС, что и на сервере)
        env: # считываем переменное окружения из GitHub Actions (см пункт 1 в инструкции)
            SECRET_KEY: ${{ secrets.DJANGO_SECRET_KEY }}
            DEBAG: ${{ secrets.DJANGO_DEBAG }}
            ALLOWED_HOSTS: ${{ secrets.DJANGO_ALLOWED_HOSTS }}
            DB_ENGINE: ${{ secrets.DB_ENGINE }}
            DB_NAME: ${{ secrets.DB_NAME }}
            DB_HOST: ${{ secrets.DB_HOST }}
            DB_PORT: ${{ secrets.DB_PORT }}
            DB_USER: ${{ secrets.DB_USER }}
            DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
        services: # подключаем нужные сервисы
            postgres_db: # название подключаемого сервиса (любое)
                image:postgres:12 # Докер образ базы постгрес
                env: # свое переменное окружение, название переменных строго заданы
                    POSTGRES_DB: ${{ env.DB_NAME }} # название БД, считанное из Secrets GitHub пунктом ранее
                    POSTGRES_USER: ${{ env.DB_USER }} # аналогично указываем все переменные из созданного ранее окружения env
                    POSTGRES_UPASSWORD: ${{ env.DB_PASSWORD }}
        ports: # указываем порты
        - 5432:5432
        options: # указываем опции для проверки 
            --health-cmd pg_isready # запускать проверки только когда постгрес уже запущен
            --health-interval 5s # запускать каждые 5 секунд
            --health-timeout 5s # если не запущен ждать 5 секунд
            --health-retries 5 # количество попыток
    steps: # описываем шаги для развертывания сервера (используем готовые модули команд GitHub и свои команды)
        - name: Проверяем репозиторий на наличие изменений
        uses: actions/checkout@v3 # команда uses для запуска готовых скриптов гитхаб эктионс, actions/checkout@v3  для проверки изменений в гитхабе

        - name: Установка python
        uses: actions/setup-python@v3 # скрипт гитхаб для установки python указанной версии и виртуального окружения
        with: # дополнительные параметры
            python-version: 3.9 # узнать поддерживаемые версии можно в документации скрипта setup-python@v3

        - name: Установка библиотек
        run: pip install -r requirements.txt # команда run для запуска, устанвоки библиотек из requirements.txt

        - name: Линтинг кода # запускаем проверку PEP8
        run: flake8 patch/ --exclude patch/migrations/ # проверка через библиотеку flake8 (не забудьте добавить ее в requirements.txt для установки) с параметром, исключающим папку с миграциями, так как ее не привести к PEP8


        - name: Тесты джанго # тесты джанго через пайтест или юнитест (сами тесты в файле test.py)
        run: python manage.py test # запуск теста из файла test.py
        env: # переменное окружение (Имена переменных как в файлах проекта settings.py)
            SECRET_KEY: ${{ env.SECRET_KEY }}
            DEBUG: ${{ env.DEBUG }}
            ALLOWED_HOSTS: ${{ env.ALLOWED_HOSTS }}
            ENGINER: ${{ env.DB_NAME }}
            DB_NAME: ${{ env.DB_NAME }}
            DB_HOST: ${{ env.DB_HOST }}
            DB_PORT: ${{ env.DB_PORT }}
            DB_USER: ${{ env.DB_USER }}
            DB_PASSWORD: ${{ env.DB_PASSWORD }}

# если запустить коммит ветки master на текущем этапе, то на гитхаб эктионс пройдут тесты, но изменения не будут загружены на сервер. Для загрузки изменений на сервер создаем еще одну команду:

      - name: Деплой # развертывание проекта на сервере
        uses: appleboy/ssh-action@master # скрипт стороннего разработчика для авторизации на сервере
        with:
            host: ${{ secrets.SSH_HOST }} # адрес сервера из github actions
            username: ${{ secrets.SSH_USER }} # пользовтаель из github actions
            password: ${{ secrets.SSH_PASSWORD }} # пароль пользователя из github actions
            script: # прописываем все команды для исполнения на сервере
#                cd /home/mihailoff/patch # переходим в папку проекта
#                git pull origin master # загружаем изменения из гит
#                source env/bin/activate - активируем созданное виртуальное окружение
#                pip install -r requirements.txt - устанавливаем нужные модули из файла requirements.txt 
#                python manage.py migrate - создаем миграции (если изменения влияют на бд)
#                sudo systemctl restart gunicorn - перезапускаем гуникорн
# Вышеописанные команды проще поместить в файл скрипта на сервере и запускать только сам скрипт
                expect /home/mihailoff/patch/deploy.exp # запускаем скрипт, описанный далее в пункте 3

```

3. Создаем файл скрипта на сервере deploy.sh
   * ssh mihailoff@44.44.44.44 - подключаемся к серверу
   * cd /home/mihailoff/patch/ - переходим в папку проекта
   * nano deploy.sh - создаем файл скрипта с расширением sh и первой строчкой #!/bin/bash
```
#!/bin/bash
cd /home/mihailoff/patch # переходим в папку проекта
git pull origin master # загружаем изменения из гит
source env/bin/activate # активируем созданное виртуальное окружение
pip install -r requirements.txt # устанавливаем нужные модули из файла requirements.txt 
python manage.py migrate # создаем миграции (если изменения влияют на бд)
sudo systemctl restart gunicorn # перезапускаем гуникорн    
```
Если запустить скрипт в таком виде, то он остановится на запросе пароля при рестарте гуникорна.
Для решения этой проблемы создаем второй файл deploy.exp 
    * cd /home/mihailoff/patch
    * pip install expect - Модуль expect вылавливает запросы в терминале
    * nano deploy.exp 
```
#!/bin/bash/expect (должен быть установлен модуль expect)
spawn /home/mihailoff/patch/deploy.sh # запустили файл скрипта
expect "password" # вылавливаем запрос пароля 
send -- "12345\r # пароль в виде сырой строки (можно тоже спрятать в виртуальном окружении)
expect eof # ждем конца скрипта
```
* sudo chmod +х deploy.sh # назначаем права файлу deploy.sh
* sudo chmod +х deploy.exp # назначаем права файлу deploy.exp
  
## Теперь при коммите ветки master, изменения будут автоматически разворачиваться на сервере


