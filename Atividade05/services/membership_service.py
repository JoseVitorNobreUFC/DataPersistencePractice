from sqlmodel import Session, select
from models import Membership

def create_membership(session: Session, membership: Membership) -> Membership:
    session.add(membership)
    session.commit()
    session.refresh(membership)
    return membership

def get_membership_by_id(session: Session, membership_id: int) -> Membership | None:
    return session.get(Membership, membership_id)

def list_memberships(session: Session) -> list[Membership]:
    return session.exec(select(Membership)).all()

def delete_membership(session: Session, membership_id: int) -> bool:
    membership = session.get(Membership, membership_id)
    if membership:
        session.delete(membership)
        session.commit()
        return True
    return False

def update_membership(session: Session, membership_id: int, membership_update: Membership) -> Membership:
    membership = session.get(Membership, membership_id)
    if not membership:
        return None

    membership_data = membership_update.model_dump(exclude_unset=True)
    for key, value in membership_data.items():
        setattr(membership, key, value)

    session.add(membership)
    session.commit()
    session.refresh(membership)
    return membership
