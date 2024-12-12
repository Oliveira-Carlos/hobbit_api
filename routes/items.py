from fastapi import APIRouter

# Cria o router para a rota de items
router = APIRouter()

# Definindo uma rota GET para listar os itens
@router.get("/")
def list_items():
    return [
        {"name": "Ring of Power", "type": "Artifact", "owner": "Sauron"},
        {"name": "Sting", "type": "Sword", "owner": "Frodo Baggins"}
    ]

# Adicionar outras rotas (como POST, PUT, DELETE, etc.)
