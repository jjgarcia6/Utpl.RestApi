import os

from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://userinventario:7kghDLHb5lSxqwpVRDmCBWA0Vd2rmGwZ@dpg-cth1a2t2ng1s739j6ovg-a.oregon-postgres.render.com/dbinventario_087f"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
