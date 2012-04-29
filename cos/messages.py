from bson import BSON


class Message(object):
    """
    Base message class. Used as a starting
    point for both Requests and Responses
    """
    headers = {}
    body = None

    def set_header(self, name, value):
        self.headers[name] = value

    def get_header(self, name, default=None):
        return self.headers.get(name, default)


class Request(Message):
    """
    Request object. Holds data from the request
    along with context data
    """

    method = None
    path = None
    context = {}

    def __init__(self, headers = {}, body = {}, path = "", method = ""):
        self.headers = headers
        self.body = body
        self.path = path
        self.method = method

    @classmethod
    def from_bson(cls, bson):
        data = BSON.decode(bson)
        if not cls._valid(data):
            raise Exception('invalid message')

        headers = data['headers']
        body = data['body']
        method = data['method']
        path = data['path']
        return cls(headers, body, path, method)

    @classmethod
    def _valid(cls, data):
        is_valid = True
        is_valid = is_valid and 'headers' in data
        is_valid = is_valid and 'path' in data
        is_valid = is_valid and 'method' in data
        is_valid = is_valid and 'body' in data
        return is_valid


class Response(Message):
    """
    Base response class
    """
    code = 200

    def set_code(code):
        self.code = int(code)

    @property
    def bson(self):
        data = {
            'code': self.code,
            'headers': self.headers,
            'body': self.body,
        }
        return BSON.encode(data)


class ErrorResponse(Exception, Response):
    """
    Generic error response.
    It can be raised as an exception
    """
    code = 400

    def __init__(self, message):
        self.body = message

    def __str__(self):
        return repr(self.body)
