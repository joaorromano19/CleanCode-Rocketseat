from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.entities.users import Users
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    def __init__(self, db_conn_handler: DbConnectionHandler):
        self.__db_conn_handler = db_conn_handler

    # Insere um novo usuário no banco de dados
    def insert_user(self, person_name: str, age: int, height: float) -> None:
        # Inicia uma sessão com o banco de dados
        with self.__db_conn_handler as database:
            try:
                # Cria um novo objeto Users com os parâmetros nome, idade e altura 
                new_user = Users(person_name=person_name, age=age, height=height)
                # Adiciona o novo usuário à sessão do banco de dados
                database.session.add(new_user)
                # Confirma a transação
                database.session.commit()
                return new_user
            # Em caso de erro, desfaz a transação
            except Exception as exception:
                database.session.rollback()
                return exception

    # Busca usuários pelo nome e retorna uma lista de resultados
    def select_user(self, person_name: str) -> list[Users]:
        # Inicia uma sessão com o banco de dados
        with self.__db_conn_handler as database:
            # Realiza a consulta no banco de dados filtrando pelo nome
            users = (
                database.session.query(Users)
                .filter(Users.person_name == person_name)
                .all()
            )
            # Retorna a lista de usuários encontrados
            return users
