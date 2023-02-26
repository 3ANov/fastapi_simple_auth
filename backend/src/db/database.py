import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@db/{db_name}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

