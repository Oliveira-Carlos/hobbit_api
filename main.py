# main.py
from fastapi import FastAPI
from routes import characters, items
from routes.auth import router as auth_router

app = FastAPI(
    title="Hobbit API",
    description="Explore a Terra Média com nossa API!",
    version="1.0.0"
)

# Conectar as rotas
app.include_router(characters.router, prefix="/characters", tags=["Characters"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à Terra Média!"}