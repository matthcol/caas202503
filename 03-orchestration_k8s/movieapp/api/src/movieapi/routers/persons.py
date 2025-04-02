from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()


@router.get("/persons/")
def list_films(db: Session = Depends(get_db)):
    return [{'name': 'moi'}, {'name': 'toi'}]

