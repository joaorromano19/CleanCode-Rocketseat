from abc import ABC, abstractmethod

class UserCreatorInterface(ABC):

    @abstractmethod
    def insert_new_user(self, person_name: str, age: int, height: float) -> dict:
        pass