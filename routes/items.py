from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Item

router = APIRouter()

# 1. GET - Listar todos os itens
@router.get("/")
def list_items(db: Session = Depends(get_db)):
    """
    Mostra todos os itens da prateleira.
    """
    items = db.query(Item).all()
    return items

# 2. POST - Criar um novo item
@router.post("/")
def create_item(name: str, type: str, attributes: str = None, description: str = None, db: Session = Depends(get_db)):
    """
    Adiciona um novo item à prateleira.
    """
    new_item = Item(name=name, type=type, attributes=attributes, description=description)
    db.add(new_item)  # Coloca o novo item no banco
    db.commit()  # Confirma que ele está na prateleira
    db.refresh(new_item)  # Atualiza o item
    return new_item

# 3. PUT - Atualizar um item
@router.put("/{item_id}")
def update_item(item_id: int, name: str = None, type: str = None, attributes: str = None, description: str = None, db: Session = Depends(get_db)):
    """
    Conserta ou atualiza um item.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado!")

    # Atualizando apenas os campos fornecidos
    if name:
        item.name = name
    if type:
        item.type = type
    if attributes:
        item.attributes = attributes
    if description:
        item.description = description

    db.commit()  # Confirma as alterações
    db.refresh(item)  # Atualiza o item na memória
    return item

# 4. DELETE - Remover um item
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Remove um item da prateleira.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado!")

    db.delete(item)  # Remove o item
    db.commit()  # Confirma a remoção
    return {"detail": "Item removido com sucesso!"}
