from pydantic import BaseModel
from typing import Optional

class LivroCreate(BaseModel):
    titulo: str
    autor: str
    ano: int
    genero: str

class LivroModel(LivroCreate):
    id: int