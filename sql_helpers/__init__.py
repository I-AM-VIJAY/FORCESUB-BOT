import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from Config import Config


def start() -> scoped_session:
    engine = create_engine(Config.DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # HEHE ABB TO MAI BHI CHANNEL PER MEMBER BADHAUNGA
    print("DATABASE_URL is not configured. Features depending on the database might have issues.")
    print(str(e))
