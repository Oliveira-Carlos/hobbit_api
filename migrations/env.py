from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy import pool
from logging.config import fileConfig
from sqlalchemy import engine_from_config

from logging.config import fileConfig
import sys
from pathlib import Path

from alembic import context

load_dotenv()

# Configuração Alembic
config = context.config

# Substituir sqlalchemy.url com a variável de ambiente DATABASE_URL
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

#Credenciais
DATABASE_URL = os.getenv("DATABASE_URL")

connectable = create_engine(DATABASE_URL)


# Adicione o caminho 
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Importando o modelo Base e os modelos do SQLAlchemy
from models import Base 
from database import DATABASE_URL 

# O objeto MetaData que Alembic precisa para gerenciar as migrações
target_metadata = Base.metadata

# Configurações do Alembic a partir do arquivo .ini
config = context.config
fileConfig(config.config_file_name)

# Função para executar as migrações
def run_migrations_offline():
    url = DATABASE_URL  # URL do banco de dados
    context.configure(url=url, target_metadata=target_metadata)
    
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Condição de execução para migrações offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
