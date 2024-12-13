from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Character

router = APIRouter()

@router.get("/")
def list_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()  # Obtém todos os personagens no banco
    return characters
