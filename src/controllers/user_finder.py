from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .interfaces.user_finder import UserFinderInterface
from ..errors.error_types.http_not_found import HttpNotFoundError


# Classe responsável por buscar usuários no repositório
class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    # Busca um usuário pelo nome e retorna a resposta formatada
    def find_user_by_person_name(self, person_name: str) -> dict:
        selected_users = self.select_and_validate_user(person_name)
        return self.__format_response(selected_users)

    # Verifica se o usuário existe e retorna a lista de usuários encontrados
    def select_and_validate_user(self, person_name: str) -> list:
        selected_users = self.__users_repository.select_user(person_name)
        # Se nenhum usuário for encontrado, lança uma exceção
        if not selected_users or len(selected_users) == 0:
            raise HttpNotFoundError("Usuário não encontrado!")
        return selected_users

    # Formata a resposta com os dados dos usuários encontrados
    def __format_response(self, selected_users: list) -> dict:
        # Cria uma lista vazia
        formatted_users = []
        # Faz uma procura dos usuarios na lista de usuarios selecionados
        for user in selected_users:
            formatted_users.append(
                {"age": user.age, "id": user.id, "person_name": user.person_name}
            )
        return {
            "Type": "Users",
            "count": len(formatted_users),
            "atributes": formatted_users,
        }
