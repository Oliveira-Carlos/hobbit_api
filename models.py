from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

# Base para os modelos
Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    race = Column(String, index=True, nullable=False)
    famous_quote = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Character(name='{self.name}', race='{self.race}', famous_quote='{self.famous_quote}')>"
