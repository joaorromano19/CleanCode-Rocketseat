import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.repositories.users_repository import UsersRepository


# pylint:disable = C0301
# @pytest -> serve para especificar para o terminal que é um teste, e nesse caso para que não cadastre um novo usuario toda vez que eu rodar o file
@pytest.mark.skip(reason="Insert into DB")
def test_users_repository():
    # Cria uma instância do manipulador de conexão com o banco de dados
    db_conn = DbConnectionHandler()
    # Cria uma instância do repositório de usuários
    users_repository = UsersRepository(db_conn)

    # Define os dados do usuário de teste
    person_name = "Meu nome de teste"
    age = 99
    height = 2.22

    # Insere o usuário no banco de dados
    users_repository.insert_user(person_name, age, height)
    # Busca o usuário pelo nome
    users = users_repository.select_user(person_name)

    # Verifica se o resultado é uma lista
    assert isinstance(users, list)
    # Verifica se apenas um usuário foi retornado
    assert len(users) == 1
    # Verifica se os dados do usuário retornado são os esperados
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height
