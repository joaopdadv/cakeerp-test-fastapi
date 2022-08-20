from http import client
import imp
from importlib.metadata import metadata
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tests.database import SQLALCHEMY_DATABASE_URL, Base, get_db
from tests.api import app


SQLALCHEMY_DATABASE_URL="sqllite///./sql_app_teste.db"

engine=create_engine(
    url=SQLALCHEMY_DATABASE_URL,
     connect_args={}
     )

testingSessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db=testingSessionLocal
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db]=override_get_db
client=TestClient(app)