import logging


from fastapi import APIRouter, Depends, HTTPException
from typing import Union

from sqlalchemy.orm import Session

from db import models, schemas, crud
from db.schemas import UserSchema
from depends import get_db

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/")
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
