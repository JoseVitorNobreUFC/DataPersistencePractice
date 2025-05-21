from sqlmodel import Session, select
from models import Projeto

def create_projeto(session: Session, projeto: Projeto) -> Projeto:
    session.add(projeto)
    session.commit()
    session.refresh(projeto)
    return projeto

def get_projeto_by_id(session: Session, projeto_id: int) -> Projeto | None:
    return session.get(Projeto, projeto_id)

def list_projetos(session: Session) -> list[Projeto]:
    return session.exec(select(Projeto)).all()

def delete_projeto(session: Session, projeto_id: int) -> bool:
    projeto = session.get(Projeto, projeto_id)
    if projeto:
        session.delete(projeto)
        session.commit()
        return True
    return False

def update_projeto(session: Session, projeto_id: int, projeto_update: Projeto) -> Projeto:
    projeto = session.get(Projeto, projeto_id)
    if not projeto:
        return None

    projeto_data = projeto_update.model_dump(exclude_unset=True)
    for key, value in projeto_data.items():
        setattr(projeto, key, value)

    session.add(projeto)
    session.commit()
    session.refresh(projeto)
    return projeto