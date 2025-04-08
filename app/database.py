from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql://fastapi_user:mysecret@localhost/contacts_db"

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаем сессию для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии из зависимости
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
