# pylint:disable = R0903

from sqlalchemy import Column, String, Integer,Float
from src.models.connection.base import Base

class Users(Base):
    # Cria uma tabela chamada Users
    __tablename__ = "users"

    # coluna do id e suas especificações
    id = Column(Integer, primary_key = True, autoincrement = True)
    # coluna nome e suas especificações
    person_name = Column(String, nullable = False)
    # coluna idade e suas especificações
    age = Column(Integer)
    # coluna altura e suas especificações
    height = Column(Float)

    # define a resposta quando ouver uma requisição de algum usuario
    def __repr__(self):
        return f"Users [id = {self.id}, person_name = {self.person_name}]"