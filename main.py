from fastapi import FastAPI
from routes import characters, items  

app = FastAPI(
    title="Hobbit API",
    description="Explore a Terra Média com nossa API!",
    version="1.0.0"
)

# Rotas 
app.include_router(characters.router, prefix="/characters", tags=["Characters"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à Terra Média!"}
