class HttpUnprocessableEntityError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.status_code = 422
        self.name = "HttpUnprocessableEntity"
        self.message = message
