from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    race = Column(String(50), nullable=False)
    quote = Column(Text, nullable=True)  # Fala do personagem  Text
    description = Column(Text, nullable=True)  # Descrição  Text
    created_at = Column(DateTime, default=datetime.utcnow)  # Data de criação
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Data de atualização

    def __repr__(self):
        return f"<Character(name={self.name}, race={self.race}, quote={self.quote})>"

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    attributes = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)  # Descrição do item Text
    created_at = Column(DateTime, default=datetime.utcnow)  # Data de criação
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Data de atualização

    def __repr__(self):
        return f"<Item(name={self.name}, type={self.type}, attributes={self.attributes})>"
