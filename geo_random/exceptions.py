class BaseShapeException(Exception):

    default_message = 'There was an exception'

    def __init__(self, message=None, *args, **kwargs):
        self.message = message or self.default_message

    def __str__(self):
        return self.message


class InvalidLineException(BaseShapeException):
    default_message = 'Invalid line: point are the same'


class MaxPointCountExceeded(BaseShapeException):
    default_message = 'Maximum point of lines was exceeded'


class InvalidCircleException(BaseShapeException):
    default_message = 'Invalid circle exception'


class InvalidSquareException(BaseShapeException):
    default_message = 'Invalid circle exception'
