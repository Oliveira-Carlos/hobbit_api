from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Garantir que a URL do banco de dados seja carregada corretamente
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não foi definida!")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)  # Adicionando pool_pre_ping para evitar falhas de conexão
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Gerenciador de contexto para trabalhar com sessões
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
