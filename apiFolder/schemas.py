import datetime
from typing import Optional
from pydantic import BaseModel

class SchemaPessoaBase(BaseModel):
    name: str
    idade: Optional[int] = None
    create_date: datetime.datetime = None

class SchemaPessoaCreate(SchemaPessoaBase):
    pass

class SchemaPessoa(SchemaPessoaBase):
    id: int

    class Config:
        orm_mode = True