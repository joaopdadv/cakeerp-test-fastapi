from urllib import response
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models import Base
from schemas import SchemaPessoa, SchemaPessoaCreate
from database import get_db, engine
from crud import get_pessoa_by_id, get_pessoas, create_pessoa, get_pessoa_by_name

from typing import List
from urllib import response

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/pessoas", response_model = List[SchemaPessoa])
def read_pessoas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pessoas = get_pessoas(db, skip=skip, limit=limit);

    return pessoas

@app.post("/pessoas", response_model = SchemaPessoa)
def write_pessoa(pessoa: SchemaPessoaCreate, db: Session = Depends(get_db)):
    return create_pessoa(db=db, pessoa=pessoa)

@app.get("/pessoas/{id}", response_model = SchemaPessoa)
def read_pessoa(id: int, db: Session = Depends(get_db)):
    db_pessoa = get_pessoa_by_id(db=db, pessoa_id=id);

    if db_pessoa is None:
        raise HTTPException(status_code=404, detail="Item not found.");

    return db_pessoa

@app.get("/pessoas/name/{name}", response_model = List[SchemaPessoa])
def read_pessoa_by_name(name: str, db: Session = Depends(get_db)):
    db_pessoa = get_pessoa_by_name(db=db, pessoa_name=name);

    if db_pessoa is None:
        raise HTTPException(status_code=404, detail="Item not found.");

    return db_pessoa

@app.get("/status")
def status():
    return {
        "message": "ok"
        }