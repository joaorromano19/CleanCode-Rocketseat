from src.models.entities.users import Users
from .user_finder import UserFinder
import pytest


# Mock que simula o repositório de usuários com retorno válido
class UserRepositoryMock:
    def __init__(self):
        # Dicionário para armazenar os parâmetros usados na chamada do método select_user
        # Isso permite verificar se o método foi chamado corretamente durante o teste
        self.select_user_att = {}

    # Simula a busca de um usuário pelo nome
    # Retorna uma lista com um objeto Users fictício, simulando um usuário encontrado
    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return [Users(id=111, person_name="jooa", age=12, height=1.7)]


# Mock que simula o repositório de usuários com retorno vazio
# Usado para testar o comportamento da aplicação quando o usuário não é encontrado
class UserRepositoryMockError:
    def __init__(self):
        # Também armazena os parâmetros usados na chamada para validação posterior
        self.select_user_att = {}

    # Simula a busca de um usuário pelo nome
    # Retorna uma lista vazia, indicando que nenhum usuário foi encontrado
    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []


# Teste que verifica o comportamento da classe UserFinder quando o usuário é encontrado
def test_find_user_by_person_name():
    person_name = "pedro"
    # Instancia o mock e injeta no UserFinder
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)

    # Executa o método que deve retornar os dados formatados do usuário
    response = user_finder.find_user_by_person_name(person_name)

    # Exibe os dados capturados pelo mock
    print(response)
    print(user_repository.select_user_att)

    # Verifica se o nome passado foi corretamente armazenado no mock
    assert user_repository.select_user_att["person_name"] == person_name
    # Verifica se a resposta é um dicionário
    assert isinstance(response, dict)
    # Verifica se o tipo retornado está correto
    assert response["Type"] == "Users"
    # Verifica se a chave "atributes" está presente na resposta
    assert "atributes" in response
    # Verifica se "atributes" é uma lista (como esperado)
    assert isinstance(response["atributes"], list)


# Teste que verifica o comportamento da classe UserFinder quando o usuário não é encontrado
def test_find_user_by_person_name_error():
    # Instancia o mock que retorna lista vazia
    user_repository = UserRepositoryMockError()
    user_finder = UserFinder(user_repository)

    # Usa pytest.raises para verificar se uma exceção é lançada corretamente
    with pytest.raises(Exception) as exe_info:
        user_finder.find_user_by_person_name("something")

    print(exe_info)

    # Verifica se a mensagem da exceção está correta
    assert str(exe_info.value) == "Usuário não encontrado!"
