from src.models.connection.db_connection_handler import DbConnectionHandler
from src.controllers.user_creator import UserCreator
from src.models.repositories.users_repository import UsersRepository
from src.view.user_creator_view import UserCreatorView

def user_creator_composer():
    conn = DbConnectionHandler()
    model = UsersRepository(conn)
    controller = UserCreator(model)
    view = UserCreatorView(controller)
    return view
