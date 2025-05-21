from sqlmodel import Session, select
from models import Membro

def create_membro(session: Session, membro: Membro) -> Membro:
    session.add(membro)
    session.commit()
    session.refresh(membro)
    return membro

def get_membro_by_id(session: Session, membro_id: int) -> Membro | None:
    return session.get(Membro, membro_id)

def list_membros(session: Session) -> list[Membro]:
    return session.exec(select(Membro)).all()

def delete_membro(session: Session, membro_id: int) -> bool:
    membro = session.get(Membro, membro_id)
    if membro:
        session.delete(membro)
        session.commit()
        return True
    return False

def update_membro(session: Session, membro_id: int, membro_update: Membro) -> Membro:
    membro = session.get(Membro, membro_id)
    if not membro:
        return None

    membro_data = membro_update.model_dump(exclude_unset=True)
    for key, value in membro_data.items():
        setattr(membro, key, value)

    session.add(membro)
    session.commit()
    session.refresh(membro)
    return membro