from typing import Optional
from sqlmodel import Field, SQLModel


class Cliente(SQLModel, table=True):
    __tablename__ : str = 'clientes'

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str 
    email: str 
    telefone: str 

    
  