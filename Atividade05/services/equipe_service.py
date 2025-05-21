from sqlmodel import Session, select
from models import Equipe

def create_equipe(session: Session, equipe: Equipe) -> Equipe:
    session.add(equipe)
    session.commit()
    session.refresh(equipe)
    return equipe

def get_equipe_by_id(session: Session, equipe_id: int) -> Equipe | None:
    return session.get(Equipe, equipe_id)

def list_equipes(session: Session) -> list[Equipe]:
    return session.exec(select(Equipe)).all()

def delete_equipe(session: Session, equipe_id: int) -> bool:
    equipe = session.get(Equipe, equipe_id)
    if equipe:
        session.delete(equipe)
        session.commit()
        return True
    return False

def update_equipe(session: Session, equipe_id: int, equipe: Equipe) -> Equipe:
    equipe = session.get(Equipe, equipe_id)
    if not equipe:
        return None
    
    equipe_data = equipe.model_dump(exclude_unset=True)
    for key, value in equipe_data.items():
        setattr(equipe, key, value)
    
    session.add(equipe_data)
    session.commit()
    session.refresh(equipe_data)
    return equipe_data

