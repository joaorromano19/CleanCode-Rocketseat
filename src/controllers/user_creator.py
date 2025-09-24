from src.controllers.interfaces.user_creator import UserCreatorInterface
from src.errors.error_types.http_bed_request import HttpBedRequestError
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface


# Classe responsável por criar usuários
class UserCreator(UserCreatorInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    # Insere um novo usuário no banco de dados
    def insert_new_user(self, person_name: str, age: int, height: float) -> dict:
        # Verifica se o usuário já existe pelo nome
        self.__check_if_user_exists(person_name)
        # Cria o novo usuário com nome, idade e altura
        self.__create_new_user(person_name, age, height)
        # Retorna a resposta de sucesso
        return self.__format_response()

    # Verifica se o usuário já está cadastrado pelo nome
    def __check_if_user_exists(self, person_name: str) -> None:
        # Busca usuários com o nome informado
        select_users = self.__users_repository.select_user(person_name)
        # Se não houver usuários com esse nome, permite a criação
        if not select_users or len(select_users) == 0:
            return

        # Se já existir, lança uma exceção
        raise HttpBedRequestError("Usuário já cadastrado")

    # Cria um novo usuário com os parâmetros nome, idade e altura
    def __create_new_user(self, person_name: str, age: int, height: float) -> None:
        self.__users_repository.insert_user(person_name, age, height)

    # Formata a resposta de sucesso após o cadastro
    def __format_response(self) -> dict:
        return {
            "Type": "Users",
            "count": 1,
            "message": "Usuário cadastrado com sucesso!",
        }
