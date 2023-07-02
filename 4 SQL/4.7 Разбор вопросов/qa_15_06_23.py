#!/usr/bin/env python
# coding: utf-8

# # Q&A
# 
# Булыгин Олег:  
# * [LinkedIn](linkedin.com/in/obulygin)  
# * [Мой канал в ТГ по Python](https://t.me/pythontalk_ru)
# * [Чат канала](https://t.me/pythontalk_chat)
# * [Блог в Телетайпе](https://teletype.in/@pythontalk)
# * [PythonTalk на Кью](https://yandex.ru/q/loves/pythontalk/)

# In[1]:


import sqlalchemy as sq
from pprint import pprint


# In[3]:


engine = sq.create_engine('postgresql://postgres:Moff390557@localhost:5432/dvdrental')
con = engine.connect()


# ## Case when
# 
# Разделите фильмы на категории:
# 
#     'без ограничений' — если у фильма рейтинг G.
#     'с ограничениями' — если у фильма любой рейтинг, кроме G.
# 
# Новое поле с категориями назовите new_rating. Сгруппируйте данные по новому полю и посчитайте среднюю цену аренды фильмов для каждой категории.

# In[7]:


res = con.execute(
'''
SELECT CASE
    WHEN rating = 'G' THEN 'без ограничений'
    WHEN rating != 'G' THEN 'с ограничениями'
    END AS new_rating,
    ROUND(AVG(rental_rate), 2)
FROM film
GROUP BY new_rating;
'''
).fetchall()

pprint(res)


# # ## Объединение таблиц, Using
# # 
# # Отберите названия уникальных жанров фильмов, в которых снималась ...

# # In[10]:


# res = con.execute(
# '''
# SELECT DISTINCT name from category c
# JOIN film_category fc ON c.category_id=fc.category_id
# JOIN film f ON fc.film_id=f.film_id
# JOIN film_actor fa ON f.film_id=fa.film_id
# JOIN actor a ON fa.actor_id=a.actor_id
# WHERE last_name = 'Wood'
# '''
# ).fetchall()

# pprint(res)


# # In[11]:


# res = con.execute(
# '''
# SELECT DISTINCT name from category 
# JOIN film_category USING(category_id)
# JOIN film USING(film_id)
# JOIN film_actor USING(film_id)
# JOIN actor USING(actor_id)
# WHERE last_name = 'Wood'
# '''
# ).fetchall()

# pprint(res)


# # "Как перехватывать сообщения об ошибках, когда мы в пайтоне обращаемся к БД?
# # Так, например, у нас обязательный атрибут name, а мы пытаемся добавить запись без этого параметра. Или мы пытаемся удалить запись, которая связана с другой таблицей. 
# # Если перехватить ответ об ошибке, то можно предпринять действия, а не просто прекратить выполнение кода на возникшей ошибке."

# # 2. ORM - из записи лекции на 20 минут не понятно как это работает. В лекции дано без пояснений, напишите это, напишите то. А как оно работает, и почему именно так нужно написать - не понятно. Такой теме хотелось бы посвятить хотя бы половина занятия с живым человеком.

# # "import psycopg2
# # 
# # 
# # def create_db(cur):
# #     """"""Добавление таблиц в БД""""""
# #     cur.execute(
# #         """"""
# #         CREATE TABLE IF NOT EXISTS users(
# #             id SERIAL PRIMARY KEY,
# #             first_name VARCHAR(50) NOT NULL,
# #             last_name VARCHAR(50) NOT NULL,
# #             email VARCHAR(50) NOT NULL
# #         );
# # 
# #         CREATE TABLE IF NOT EXISTS phones(
# #             id SERIAL PRIMARY KEY,
# #             phone VARCHAR(15),
# #             user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
# #         );
# #         """"""
# #     )
# # 
# # 
# # def add_client(cur, first_name=None, last_name=None, email=None, phones=None):
# #     """"""Добавление клиента в БД""""""
# #     cur.execute(
# #         """"""
# #         INSERT INTO users
# #         (first_name, last_name, email)
# #         VALUES (%s, %s, %s) RETURNING id, first_name, last_name, email
# #         """""",
# #         (first_name, last_name, email),
# #     )
# #     users_res = cur.fetchone()
# #     print(f""В USERS добавлен {users_res}"")
# # 
# #     if phones:
# #         cur.execute(
# #             """"""
# #             INSERT INTO phones
# #             (phone, user_id) VALUES (%s, %s) RETURNING id, phone, user_id
# # 
# #             """""",
# #             (phones, users_res[0]),
# #         )
# # 
# #         print(f""В PHONES добавлен телефон: {cur.fetchone()}"")
# # 
# # 
# # def add_phone(cur, client_id, phone):
# #     """"""Добавление телефона""""""
# #     cur.execute(
# #         """"""
# #         INSERT INTO phones (phone, user_id) VALUES (%s, %s) RETURNING id, phone, user_id
# #         """""",
# #         (phone, client_id),
# #     )
# #     print(f""В PHONES добавлен телефон: {cur.fetchone()}"")
# # 
# # 
# # def change_client(
# #     cur, client_id, first_name=None, last_name=None, email=None, phones=None
# # ):
# #     """"""Изменение данных клиента""""""
# #     if first_name:
# #         cur.execute(
# #             """"""
# #         UPDATE users SET first_name=%s WHERE id=%s;
# #         """""",
# #             (first_name, client_id),
# #         )
# # 
# #     if last_name:
# #         cur.execute(
# #             """"""
# #         UPDATE users SET last_name=%s WHERE id=%s;
# #         """""",
# #             (last_name, client_id),
# #         )
# # 
# #     if email:
# #         cur.execute(
# #             """"""
# #         UPDATE users SET email=%s WHERE id=%s;
# #         """""",
# #             (email, client_id),
# #         )
# # 
# #     if phones:
# #         cur.execute(
# #             """"""
# #             DELETE FROM phones
# #             WHERE user_id=%s
# #             """""",
# #             (client_id),
# #         )
# # 
# #         cur.execute(
# #             """"""
# #             INSERT INTO phones (phone, user_id)
# #             VALUES (%s, %s) RETURNING user_id, phone
# #             """""",
# #             (phones, client_id),
# #         )
# #         print(f""Изменен телефон: {cur.fetchone()}"")
# # 
# #     cur.execute(
# #         """"""
# #         SELECT u.id, u.first_name, u.last_name, u.email, p.phone
# #         FROM users as u JOIN phones as p ON u.id = p.user_id
# #         WHERE u.id=%s;
# #         """""",
# #         (client_id),
# #     )
# #     print(f""Изменены данные в USERS: {cur.fetchone()}"")
# # 
# # 
# # def delete_phone(cur, client_id, phone):
# #     """"""Удаление телефона""""""
# #     cur.execute(
# #         """"""
# #         DELETE FROM phones
# #         WHERE user_id=%s AND phone=%s RETURNING id, phone, user_id
# #         """""",
# #         (client_id, phone),
# #     )
# #     print(f""Удален номер: {cur.fetchone()}"")
# # 
# # 
# # def delete_client(cur, client_id):
# #     """"""Удаление клиента по ID""""""
# #     cur.execute(
# #         """"""
# #         DELETE FROM users
# #         WHERE id=%s RETURNING id, first_name, last_name, email
# #         """""",
# #         (client_id),
# #     )
# #     print(f""Удален клиент: {cur.fetchone()}"")
# # 
# # 
# # def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
# #     """"""Поиск клиента""""""
# #     if first_name is None:
# #         first_name = ""%""
# #     else:
# #         first_name = ""%"" + first_name + ""%""
# # 
# #     if last_name is None:
# #         last_name = ""%""
# #     else:
# #         last_name = ""%"" + last_name + ""%""
# # 
# #     if email == None:
# #         email = ""%""
# #     else:
# #         email = ""%"" + email + ""%""
# # 
# #     if phone is None:
# #         phone = ""%""
# #     else:
# #         phone = ""%"" + phone + ""%""
# # 
# #     cur.execute(
# #         """"""
# #         SELECT us.id, us.first_name, us.last_name, us.email, STRING_AGG(p.phone, ' OR ')
# #         FROM users AS us JOIN phones AS p ON us.id = p.user_id
# #         WHERE us.first_name LIKE %s AND us.last_name LIKE %s AND us.email LIKE %s AND p.phone LIKE %s
# #         GROUP BY us.id
# #         """""",
# #         (first_name, last_name, email, phone),
# #     )
# # 
# #     res = cur.fetchall()
# #     for client in res:
# #         print(
# #             f""ID: {client[0]} | Name: {client[1]} | Surname: {client[2]} | Email: {client[3]} | Phone: {client[4]}""
# #         )
# # 
# # 
# # def drop_all_tables(cur):
# #     """"""Удаление всех таблиц из БД""""""
# #     cur.execute(
# #         """"""
# #         DROP TABLE phones;
# #         DROP TABLE users;
# #         """"""
# #     )
# # 
# # 
# # if __name__ == ""__main__"":
# #     with psycopg2.connect(
# #         database=""clients_db"", user=""postgres"", password=""baraguz""
# #     ) as conn:
# #         with conn.cursor() as cur:
# #             drop_all_tables(cur)
# # 
# #             create_db(cur)
# # 
# #             add_client(
# #                 cur,
# #                 first_name=""Yura"",
# #                 last_name=""Kholodov"",
# #                 email=""yuyuyuyuy@mail.ru"",
# #                 phones=""3243432545"",
# #             )
# #             add_client(
# #                 cur,
# #                 first_name=""Misha"",
# #                 last_name=""Kholodov"",
# #                 email=""ddvsvsd@mail.ru"",
# #                 phones=""2113124214"",
# #             )
# #             add_client(
# #                 cur,
# #                 first_name=""Фудзи"",
# #                 last_name=""Yama"",
# #                 email=""dsdsv@mail.ru"",
# #                 phones=""+7-5958-5858"",
# #             )
# # 
# #             change_client(
# #                 cur,
# #                 client_id=""2"",
# #                 first_name=""Николай"",
# #                 last_name=""Зайцев"",
# #                 phones=""777-777"",
# #             )
# # 
# #             add_phone(cur, client_id=""3"", phone=""12345-12345"")
# # 
# #             delete_phone(cur, client_id=""2"", phone=""777-777"")
# # 
# #             delete_client(cur, client_id=""1"")
# # 
# #             find_client(cur, first_name=""Фудзи"")
# # 
# # 
# # 
# # Вопрос 1:
# # def create_db(cur)
# # Как по дефолту в поле задать значение. Вроде пишу DEFAULT 'Имя не задано!'
# # Но реакции никакой. В поле как вставлялось Null так и вставляется!
# # Вопрос 2:
# # def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
# #     """"""Поиск клиента""""""
# # Так и не получилось сделать поиск если одно из полей None. LIKE '%' не находит None!!! Т.Е. если  хоть одно поле None, клиент не найдется! Почему так?
# # "

# # https://realpython.com/prevent-python-sql-injection/#passing-safe-query-parameters

# # "Добрый день! Подскажите, пожалуйста, какой инструмент (расширение или плагин для DBeaver и/или VSCode) для форматирования SQL-кода в соответствии с SQL Style Guide (https://www.sqlstyle.guide/ru/) могли бы порекомендовать? 
# # Пока удалось найти только расширения без возможности детальной настройки параметров форматирования - а без этого не получается автоматически отформатировать код в соответствии с SQL Style Guide (например, понравился представленный там подход к оформлению основных ключевых слов как первого столбца (за счет табуляции), названий таблиц/столбцов как второго и т.д., и ещё рекомендации по форматированию DDL-кода)."

# # ## Подзапросы
# # 
# # Проанализируйте данные о возрастных рейтингах 40 фильмов с максимальной продолжительностью, у которых стоимость проката больше 2. Выгрузите в итоговую таблицу следующие поля:
# # 
# #     возрастной рейтинг (поле rating);
# #     минимальное и максимальное значения длительности (поле length); назовите поля min_length и max_length соответственно;
# #     среднее значение длительности (поле length); назовите поле avg_length;
# #     минимум, максимум и среднее для цены просмотра (поле rental_rate); назовите поля min_rental_rate, max_rental_rate, avg_rental_rate соответственно.
# # 
# # Отсортируйте среднюю длительность фильма по возрастанию.

# # In[12]:


# res = con.execute(
# """
# SELECT top.rating,
#        MIN(top.length) AS min_length,
#        MAX(top.length) AS max_length,
#        AVG(top.length) AS avg_length,
#        MIN(top.rental_rate) AS min_rental_rate,
#        MAX(top.rental_rate) AS max_rental_rate,
#        AVG(top.rental_rate) AS avg_rental_rate
# FROM
#   (SELECT title,
#           rental_rate,
#           length,
#           rating
#    FROM film
#    WHERE rental_rate > 2
#    ORDER BY length DESC
#    LIMIT 40) AS top
# GROUP BY top.rating
# ORDER BY avg_length;
# """).fetchall()
# res


# # In[13]:


# res = con.execute(
# """
# WITH top as (SELECT title,
#           rental_rate,
#           length,
#           rating
#    FROM film
#    WHERE rental_rate > 2
#    ORDER BY length DESC
#    LIMIT 40)
# SELECT top.rating,
#        MIN(top.length) AS min_length,
#        MAX(top.length) AS max_length,
#        AVG(top.length) AS avg_length,
#        MIN(top.rental_rate) AS min_rental_rate,
#        MAX(top.rental_rate) AS max_rental_rate,
#        AVG(top.rental_rate) AS avg_rental_rate
# FROM top
# GROUP BY top.rating
# ORDER BY avg_length;
# """).fetchall()
# res


# # In[14]:


# import pandas as pd


# # In[15]:


# engine = sq.create_engine('postgresql://postgres:admin@localhost:5432/netology_bd')
# con = engine.connect()


# # In[16]:


# data = pd.read_csv('diabetes.csv')
# data


# # In[17]:


# data.to_sql(name='diabetes', con=con, index=False, if_exists='replace')


# # In[18]:


# diabetes = pd.read_sql('select * from diabetes', con)
# con.close()


# # In[19]:


# diabetes


# # In[20]:


# diabetes.info()


# # In[21]:


# diabetes.describe()


# # In[23]:


# diabetes.groupby('Outcome')['Insulin'].mean()


# # In[24]:


# import seaborn as sns

# sns.boxplot(data=diabetes, x='Outcome', y='Glucose')diabetes


# # Есть ли необходимость в первичном ключе у связующих таблиц. И если да, то для чего

# # In[ ]:


# # primary key(artist_id, track_id)


# # "Как подсчитать количество слов в поле?
# # Задание 2, пункт 4
# # Задание: https://github.com/netology-code/py-homeworks-db/tree/SQLPY-76/04-dml"

# # "Можно ли написать запрос, который выведет список всех альбомов и исполнителей в каждом из них?
# # Например,
# # альбом 1 -> исполнитель 1, исполнитель 2;
# # альбом 2 -> исполнитель 3"

# # ## ORM

# # In[28]:


# import sqlalchemy as sq
# from sqlalchemy.orm import declarative_base, relationship, sessionmaker, CheckConstraint
# import datetime as dt
# from sqlalchemy import or_


# # In[29]:


# engine = sq.create_engine('postgresql://postgres:admin@localhost:5432/netology_bd')


# # In[39]:


# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
    
#     id = sq.Column(sq.BigInteger, primary_key=True)
#     username = sq.Column(sq.String(50), unique=True)
    
#     favourite_notes = relationship('Note', secondary='favourites', back_populates='favourite_users')
    
#     def __str__(self):
#         return f'User: {self.username}'
    
# #     __table_args__ = CheckConstraint('username' ==)
    

# class Note(Base):
#     __tablename__ = 'notes'
    
#     id = sq.Column(sq.BigInteger, primary_key=True)
#     text = sq.Column(sq.UnicodeText, nullable=False)
#     public = sq.Column(sq.Boolean, default=False)
#     created_at = sq.Column(sq.DateTime, default=dt.datetime.now)
#     author_id = sq.Column(sq.BigInteger, sq.ForeignKey('users.id', ondelete='CASCADE'))
    
#     author = relationship('User', backref='notes')
#     favourite_users = relationship('User', secondary='favourites', back_populates='favourite_notes')
    
#     def __str__(self):
#         return f'Note: {self.text}'
    
    
# favourites = sq.Table(
#     'favourites', Base.metadata,
#     sq.Column('user_id', sq.BigInteger, sq.ForeignKey('users.id', ondelete='CASCADE')),
#     sq.Column('note_id', sq.BigInteger, sq.ForeignKey('notes.id', ondelete='CASCADE'))
# )

# class Service:
#     def __init__(self, session):
#         self.session = session
        
#     def create_user(self, username):
#         user = User(username=username)
#         self.session.add(user)
#         self.session.commit()
        
#         return user

#     def create_note(self, author, text, public=False):
#         note = Note(author_id=author.id, text=text, public=public)
#         self.session.add(note)
#         self.session.commit()
        
#         return note
    
#     def list_notes(self, user):

#         return self.session.query(Note).join(User).filter(
#         or_(Note.public==True, User.id==user.id)).all()
    
    

# def recreate_tables(session, engine):
#     with engine.connect() as con:
#         con.execute('DROP TABLE IF EXISTS notes CASCADE')
#         con.execute('DROP TABLE IF EXISTS users CASCADE')
#         con.execute('DROP TABLE IF EXISTS favourites CASCADE')
#     Base.metadata.create_all(engine)
    
# Session = sessionmaker(bind=engine)
# # session = Session()

# with Session() as session:
#     recreate_tables(session, engine)
#     service = Service(session)
    
#     user1 = service.create_user('user1')
#     user2 = service.create_user('user2')
    
#     note1 = service.create_note(user1, 'some public note', True)
#     note2 = service.create_note(user2, 'some private note2', False)
    
#     note3 = service.create_note(user2, 'some private note3', False)
    
#     for n in service.list_notes(user1):
#         print(n)
#     print('---------------------')
#     for n in service.list_notes(user2):
#         print(n)


# # In[ ]:




