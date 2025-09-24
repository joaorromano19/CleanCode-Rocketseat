from src.controllers.interfaces.user_creator import UserCreatorInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from ..errors.error_handler import handle_errors
from ..validators.user_creator_validator import user_creator_validator


class UserCreatorView:
    def __init__(self, controller: UserCreatorInterface):
        self.__controller = controller

    def handle_insert_new_user(self,  request: HttpRequest) -> HttpResponse:
        try:
            user_creator_validator(request)
            
            person_name = request.body["person_name"]
            age = request.body["age"]
            height = request.body["height"]

            response = self.__controller.insert_new_user(person_name, age, height)

            return HttpResponse(
                status_code = 200,
                body = response
            )
        except Exception as exception:
            return handle_errors(exception)
