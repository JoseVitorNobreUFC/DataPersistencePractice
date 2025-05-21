from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Tarefa
from services import tarefa_service

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

@router.post("/", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa, session: Session = Depends(get_session)):
    return tarefa_service.create_tarefa(session, tarefa)

@router.get("/", response_model=list[Tarefa])
def listar_tarefas(session: Session = Depends(get_session)):
    return tarefa_service.list_tarefas(session)

@router.get("/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int, session: Session = Depends(get_session)):
    tarefa = tarefa_service.get_tarefa_by_id(session, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.delete("/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, session: Session = Depends(get_session)):
    if not tarefa_service.delete_tarefa(session, tarefa_id):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa deletada com sucesso"}

@router.put("/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa, session: Session = Depends(get_session)):
    tarefa_atualizada = tarefa_service.update_tarefa(session, tarefa_id, tarefa.dict(exclude_unset=True))
    if not tarefa_atualizada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada