from fastapi import APIRouter

# Cria o router para a rota de characters
router = APIRouter()

@router.get("/")
def list_characters():
    return [{"name": "Frodo", "race": "Hobbit", "role": "Ring Bearer"}]
