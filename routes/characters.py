from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Character

router = APIRouter()

# 1. GET - Listar todos os personagens
@router.get("/")
def list_characters(db: Session = Depends(get_db)):
    """
    Mostra todos os personagens 
    """
    characters = db.query(Character).all()
    return characters

# 2. POST - Criar um novo personagem
@router.post("/")
def create_character(name: str, race: str, quote: str = None, description: str = None, db: Session = Depends(get_db)):
    """
    Adiciona um novo personagem
    """
    new_character = Character(name=name, race=race, quote=quote, description=description)
    db.add(new_character)  # Coloca o novo personagem no banco
    db.commit()  # Confirma que ele está na prateleira
    db.refresh(new_character)  # Atualiza o personagem
    return new_character

# 3. PUT - Atualizar um personagem
@router.put("/{character_id}")
def update_character(character_id: int, name: str = None, race: str = None, quote: str = None, description: str = None, db: Session = Depends(get_db)):
    """
    Conserta ou atualiza um personagem.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Personagem não encontrado!")

    # Atualizando apenas os campos fornecidos
    if name:
        character.name = name
    if race:
        character.race = race
    if quote:
        character.quote = quote
    if description:
        character.description = description

    db.commit()  # Confirma as alterações
    db.refresh(character)  # Atualiza o personagem na memória
    return character

# 4. DELETE - Remover um personagem
@router.delete("/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    """
    Remove um personagem 
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Personagem não encontrado!")

    db.delete(character)  # Remove o personagem
    db.commit()  # Confirma a remoção
    return {"detail": "Personagem removido com sucesso!"}
