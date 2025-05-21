from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Projeto
from services import projeto_service

router = APIRouter(prefix="/projetos", tags=["Projetos"])

@router.post("/", response_model=Projeto)
def criar_projeto(projeto: Projeto, session: Session = Depends(get_session)):
    return projeto_service.create_projeto(session, projeto)

@router.get("/", response_model=list[Projeto])
def listar_projetos(session: Session = Depends(get_session)):
    return projeto_service.list_projetos(session)

@router.get("/{projeto_id}", response_model=Projeto)
def buscar_projeto(projeto_id: int, session: Session = Depends(get_session)):
    projeto = projeto_service.get_projeto_by_id(session, projeto_id)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto

@router.delete("/{projeto_id}")
def deletar_projeto(projeto_id: int, session: Session = Depends(get_session)):
    if not projeto_service.delete_projeto(session, projeto_id):
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return {"message": "Projeto deletado com sucesso"}

@router.put("/{projeto_id}", response_model=Projeto)
def atualizar_projeto(projeto_id: int, projeto: Projeto, session: Session = Depends(get_session)):
    projeto_atualizado = projeto_service.update_projeto(session, projeto_id, projeto.dict(exclude_unset=True))
    if not projeto_atualizado:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto_atualizado