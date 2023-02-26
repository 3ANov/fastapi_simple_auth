from typing import List

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, Session

from db import models, schemas
from db.database import engine
from db.models import User

# Session = sessionmaker(engine)
#
#
# def add_user(user: User):
#     with Session.begin() as session:
#         session.add(user)
#
#
# def get_user(id: int):
#     stmt = select(User).where(User.id == id)
#     with Session.begin() as session:
#         return session.execute(stmt)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserSchema):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name,
                          email=user.email,
                          password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
