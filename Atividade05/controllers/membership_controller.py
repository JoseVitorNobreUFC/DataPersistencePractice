from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Membership
from services import membership_service

router = APIRouter(prefix="/memberships", tags=["Memberships"])

@router.post("/", response_model=Membership)
def criar_membership(membership: Membership, session: Session = Depends(get_session)):
    return membership_service.create_membership(session, membership)

@router.get("/", response_model=list[Membership])
def listar_memberships(session: Session = Depends(get_session)):
    return membership_service.list_memberships(session)

@router.get("/{membership_id}", response_model=Membership)
def buscar_membership(membership_id: int, session: Session = Depends(get_session)):
    membership = membership_service.get_membership_by_id(session, membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    return membership

@router.delete("/{membership_id}")
def deletar_membership(membership_id: int, session: Session = Depends(get_session)):
    if not membership_service.delete_membership(session, membership_id):
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    return {"message": "Membership deletado com sucesso"}

@router.put("/{membership_id}", response_model=Membership)
def atualizar_membership(membership_id: int, membership: Membership, session: Session = Depends(get_session)):
    membership_atualizado = membership_service.update_membership(session, membership_id, membership)
    if not membership_atualizado:
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    return membership_atualizado