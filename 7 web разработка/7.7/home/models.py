import os
import datetime
import atexit

from sqlalchemy import JSON, create_engine, DateTime, String, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped



POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRS_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRS_PORT}/{POSTGRES_DB}"


engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class User(Base):
    
    __tablename__ = "app_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    registration_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'registration_time': self.registration_time.isoformat(),
        }


Base.metadata.create_all(bind=engine) # проводим миграцию, код дойдя до этой строчки создат вышеобозначенную таблицу User
atexit.register(engine.dispose) # при завершении приложения подключение engine разорвется
