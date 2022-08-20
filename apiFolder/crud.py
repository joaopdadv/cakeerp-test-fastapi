from sqlalchemy.orm import Session

from models import Pessoa 
from schemas import SchemaPessoa, SchemaPessoaBase, SchemaPessoaCreate

def get_pessoas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pessoa).offset(skip).limit(limit).all()

def get_pessoa_by_id(db: Session, pessoa_id: int):
    return db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()

def get_pessoa_by_name(db: Session, pessoa_name: str):
    return db.query(Pessoa).filter(Pessoa.name == pessoa_name).all()

def create_pessoa(db: Session, pessoa: SchemaPessoaCreate):
    db_pessoa = Pessoa(**pessoa.dict())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)

    return db_pessoa

    