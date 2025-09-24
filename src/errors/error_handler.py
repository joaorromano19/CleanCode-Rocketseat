from ..view.http_types.http_response import HttpResponse
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_bed_request import HttpBedRequestError
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBedRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "datail": error.message}]},
        )

    return HttpResponse(
        status_code = 500,
        body={"errors": [{"title": "Server error!", "datail": str(error)}]},
    )
