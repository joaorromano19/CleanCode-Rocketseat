from abc import ABC, abstractmethod
from src.models.entities.users import Users

# É uma classe abstrata, ou seja, sempre que for implementada em alguma outra classe, vai "obrigar" a classe a ter os metodos que estão dentro da classe abstrata
class UsersRepositoryInterface(ABC):
    @abstractmethod
    # Insere usuarios no banco de dados
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        pass
    @abstractmethod
    # Busca os usuarios no banco de dados
    def select_user(self, person_name: str) -> list[Users]:
        pass