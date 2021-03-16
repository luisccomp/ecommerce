class HttpError(Exception):

    def __init__(self, status=500, message='Internal server error', details=None):
        self.status = status
        self.message = message
        self.details = details

    @classmethod
    def bad_request(cls, message='Bad request', details=None):
        return cls(400, message, details)

    @classmethod
    def not_found(cls, message='Not found', details=None):
        return cls(404, message, details)

    @classmethod
    def unauthorized(cls, message='Unauthorized', details=None):
        return cls(401, message, details)


def handle_http_errors(e):
    return {
        'status': e.status,
        'message': e.message,
        'details': e.details
    }, e.status
