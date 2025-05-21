from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Membro
from services import membro_service

router = APIRouter(prefix="/membros", tags=["Membros"])

@router.post("/", response_model=Membro)
def criar_membro(membro: Membro, session: Session = Depends(get_session)):
    return membro_service.create_membro(session, membro)

@router.get("/", response_model=list[Membro])
def listar_membros(session: Session = Depends(get_session)):
    return membro_service.list_membros(session)

@router.get("/{membro_id}", response_model=Membro)
def buscar_membro(membro_id: int, session: Session = Depends(get_session)):
    membro = membro_service.get_membro_by_id(session, membro_id)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro

@router.delete("/{membro_id}")
def deletar_membro(membro_id: int, session: Session = Depends(get_session)):
    if not membro_service.delete_membro(session, membro_id):
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return {"message": "Membro deletado com sucesso"}

@router.put("/{membro_id}", response_model=Membro)
def atualizar_membro(membro_id: int, membro: Membro, session: Session = Depends(get_session)):
    membro_atualizado = membro_service.update_membro(session, membro_id, membro)
    if not membro_atualizado:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro_atualizado