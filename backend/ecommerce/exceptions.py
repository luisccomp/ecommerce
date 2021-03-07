from os import environ


class BaseHttpException(Exception):

    def __init__(self, status=500, message='Internal server error', details=None):
        super().__init__()
        self.status = status
        self.message = message
        self.details = details


class NotFoundException(BaseHttpException):

    def __init__(self, message='Not Found', details=None):
        super().__init__(status=404, message=message, details=details)


def handle_base_http_exception(e: BaseHttpException):
    return {
        'status': e.status,
        'message': e.message,
        'details': e.details
    }, e.status
