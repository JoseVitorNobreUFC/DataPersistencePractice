from livro_repository import (
    get_all_records,
    get_record_by_id,
    create_record,
    update_record,
    delete_record,
    get_next_id
)
from livro_model import LivroCreate, LivroModel
from typing import Dict
from fastapi import HTTPException

LIVRO_XML_PATH = './livros.xml'

def get_all_livros():
    return get_all_records(LIVRO_XML_PATH)

def get_livro_by_id(livro_id: int):
    livro = get_record_by_id(LIVRO_XML_PATH, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

def create_livro(livro: LivroCreate):
    novo_livro = LivroModel(id=get_next_id(LIVRO_XML_PATH), **livro.dict())
    ordered_data: Dict[str, str] = {
        "id": str(novo_livro.id),
        "titulo": novo_livro.titulo,
        "autor": novo_livro.autor,
        "ano": str(novo_livro.ano),
        "genero": novo_livro.genero
    }
    return create_record(LIVRO_XML_PATH, ordered_data)

def update_livro(livro_id: int, livro: LivroCreate):
    if not get_record_by_id(LIVRO_XML_PATH, livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    updated_data: Dict[str, str] = {
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano": str(livro.ano),
        "genero": livro.genero
    }
    success = update_record(LIVRO_XML_PATH, livro_id, updated_data)
    if not success:
        raise HTTPException(status_code=500, detail="Erro ao atualizar livro")
    return True

def delete_livro(livro_id: int):
    if not get_record_by_id(LIVRO_XML_PATH, livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    success = delete_record(LIVRO_XML_PATH, livro_id)
    if not success:
        raise HTTPException(status_code=500, detail="Erro ao deletar livro")
    return True
