from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Item

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtém todos os itens no banco
    return items
