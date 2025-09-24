from .user_creator import UserCreator
import pytest


# Classe mock usada para testar os métodos sem acessar o BD real
class UserRepositoryMock:
    # Armazena os dados utilizados nos métodos para verificação posterior
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    # Simula a busca de um usuário pelo nome, retornando uma lista vazia para indicar que o usuário não existe
    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

    # Simula a inserção de um novo usuário no "BD" falso
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        self.insert_user_att["person_name"] = person_name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height

class UserRepositoryMockError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [1, 2, 3]


# Testa o processo de inserção de um novo usuário usando o mock
def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    # Dados do usuário de teste
    person_name = "joao"
    age = 17
    height = 1.87

    # Executa o método de inserção
    response = user_creator.insert_new_user(person_name, age, height)

    # Exibe os dados capturados pelo mock
    print(response)
    print(user_repository.select_user_att)
    print(user_repository.insert_user_att)

    # Verifica se os dados foram corretamente utilizados
    assert user_repository.select_user_att["person_name"] == person_name
    assert user_repository.insert_user_att["person_name"] == person_name
    assert user_repository.insert_user_att["age"] == age
    assert user_repository.insert_user_att["height"] == height

    # Verifica se a resposta está no formato esperado
    assert isinstance(response, dict)
    assert "Type" in response
    assert response["count"] == 1
    # assert response["message"] == "Usuário cadastrado com sucesso!"


def test_insert_new_user_error():
    user_repository = UserRepositoryMockError()
    user_creator = UserCreator(user_repository)

    with pytest.raises(Exception) as exe_info:
        user_creator.insert_new_user("something", 22, 3.3)

    print(exe_info.value)     
    assert str(exe_info.value) == "Usuário já cadastrado"     
