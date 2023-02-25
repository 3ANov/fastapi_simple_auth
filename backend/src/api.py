import logging
import os
from fastapi import APIRouter
from typing import Union

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
def read_root():
    logger.debug(os.getenv('POSTGRES_USER'))
    return {"Hello": "World2"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}