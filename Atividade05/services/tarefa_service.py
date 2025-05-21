from sqlmodel import Session, select
from models import Tarefa

def create_tarefa(session: Session, tarefa: Tarefa) -> Tarefa:
    session.add(tarefa)
    session.commit()
    session.refresh(tarefa)
    return tarefa

def get_tarefa_by_id(session: Session, tarefa_id: int) -> Tarefa | None:
    return session.get(Tarefa, tarefa_id)

def list_tarefas(session: Session) -> list[Tarefa]:
    return session.exec(select(Tarefa)).all()

def delete_tarefa(session: Session, tarefa_id: int) -> bool:
    tarefa = session.get(Tarefa, tarefa_id)
    if tarefa:
        session.delete(tarefa)
        session.commit()
        return True
    return False

def update_tarefa(session: Session, tarefa_id: int, tarefa_data: dict) -> Tarefa:
    tarefa = session.get(Tarefa, tarefa_id)
    if not tarefa:
        return None

    tarefa_data = tarefa.model_dump(exclude_unset=True)
    for key, value in tarefa_data.items():
        setattr(tarefa, key, value)

    session.add(tarefa_data)
    session.commit()
    session.refresh(tarefa_data)
    return tarefa_data