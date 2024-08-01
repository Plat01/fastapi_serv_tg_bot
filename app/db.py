from sqlalchemy import create_engine
from sqlmodel import Session, select

from app.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    # Not necessary if Alembic used
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)



