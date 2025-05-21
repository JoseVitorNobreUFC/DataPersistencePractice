from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Equipe
from services import equipe_service

router = APIRouter(prefix="/equipes", tags=["Equipes"])

@router.post("/", response_model=Equipe)
def criar_equipe(equipe: Equipe, session: Session = Depends(get_session)):
    return equipe_service.create_equipe(session, equipe)

@router.get("/", response_model=list[Equipe])
def listar_equipes(session: Session = Depends(get_session)):
    return equipe_service.list_equipes(session)

@router.get("/{equipe_id}", response_model=Equipe)
def buscar_equipe(equipe_id: int, session: Session = Depends(get_session)):
    equipe = equipe_service.get_equipe_by_id(session, equipe_id)
    if not equipe:
        raise HTTPException(status_code=404, detail="Equipe não encontrada")
    return equipe

@router.delete("/{equipe_id}")
def deletar_equipe(equipe_id: int, session: Session = Depends(get_session)):
    success = equipe_service.delete_equipe(session, equipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Equipe não encontrada")
    return {"message": "Equipe deletada com sucesso"}

@router.put("/{equipe_id}", response_model=Equipe)
def atualizar_equipe(equipe_id: int, equipe: Equipe, session: Session = Depends(get_session)):
    equipe_atualizada = equipe_service.update_equipe(session, equipe_id, equipe)
    if not equipe_atualizada:
        raise HTTPException(status_code=404, detail="Equipe não encontrada")
    return equipe_atualizada
