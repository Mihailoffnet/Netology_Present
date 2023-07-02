import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Course(Base):
    __tablename__ = "course"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # homeworks = relationship("Homework", back_populates="course")
    def __str__(self):
        return f'Курс {self.id}: {self.name}'


class Homework(Base):
    __tablename__ = "homework"

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    course = relationship(Course, backref="homeworks")

    def __str__(self):
        return f'Домашняя работа {self.id}: {self.number} - {self.description} по курсу {self.course_id}'


def create_tables(engine):
    Base.metadata.drop_all(engine) # - Удаление таблицы (всех таблиц, ALL)
    Base.metadata.create_all(engine) # - создание таблицы (не будет ошибки, если таблица уже создана)

# DSN = "postgresql://логин:пароль@localhost:5432/имя_базы"
DSN = "postgresql://postgres:Moff390557@localhost:5432/test"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
course1 = Course(name="JavaScript")
course2 = Course(name="Python from Zero")

hw1 = Homework(number=1, description="простая домашняя работа", course=course1)
hw2 = Homework(number=2, description="сложная домашняя работа", course=course2)
hw3 = Homework(number=3, description="Сложная домашняя работа по Java", course=course2)

session.add(course1) # добавляем курс course1
session.add(course2) # добавляем курс course1
print('course1', course1.id) # None - пока не закомиттили изменения session.commit() 
session.add_all([hw1, hw2]) # можно добавить все сразу, из списка
session.commit()  # фиксируем изменения
print('course1', course1.id) # после фиксации изменений id можно вызвать
print('course1', course1)
print('course2', course2)
print()
print('hw1', hw1)
print('hw2', hw2)
print('hw2', hw3)
print()

# запросы
for c in session.query(Homework).filter(Homework.number != 1).all():
    print(f'ДЗ с номером больше 1 - {c}')

print()

for c in session.query(Homework).filter(Homework.description.ilike('%сложн%')).all():
    print(f'ДЗ с словом "Сложн" - {c}')

print()

q = session.query(Course).join(Homework.course).filter(Homework.number != 2)
print(f'посмотреть SQL запрос:\n{q}') # посмотреть SQL запрос
print()
for s in q.all():
    print(s.id, s.name)
    for hw in s.homeworks:
        print("\t", hw.id, hw.number, hw.description)

print()

# вложенный запрос
subq = session.query(Homework).filter(Homework.description.ilike('%сложн%')).subquery()
q = session.query(Course).join(subq, Course.id == subq.c.course_id) # результаты подзапроса хранятся в поле "c", такая особенность
print(f'посмотреть SQL запрос с вложенным запросом:\n{q}') # посмотреть SQL запрос
print()
print(f'Курсы с ДЗ, где есть слово "Сложн"')
for s in q.all():
    print(s.id, s.name)
    for hw in s.homeworks:
        print("\t", hw.id, hw.number, hw.description)

print()

# обновление объектов
session.query(Course).filter(Course.name == "JavaScript").update({"name": "New JavaScript"})
session.commit()  # фиксируем изменения 
print(f'Новое название курса {course1}')
print()

# удаление объектов
session.query(Homework).filter(Homework.number == 1).delete()
session.commit()  # фиксируем изменения
q = session.query(Homework)
for s in q.all():
    print(f'ДЗ: {s}')
print()

session.query(Course).filter(Course.name.ilike('%java%')).delete()
session.commit()  # фиксируем изменения
q = session.query(Course)
for s in q.all():
    print(f'Курсы: {s}')
print()

session.close() # закрываем сессию
