from cos.messages import Request, Response


class Repository(object):

    handlers = []

    def add_handler(self, handler):
        if hasattr(handler,
            'process_request') or hasattr(handler,
            'process_response'):
            self.handlers.append(handler)
        else:
            raise Error("Middleware must provide a process_request and/or a process_response method")

    def process_request(self, request):
        for handler in self.handlers:
            if hasattr(handler, 'process_request'):
                handler.process_request(request)

    def process_response(self, request, response):
        for handler in self.handlers:
            if hasattr(handler, 'process_response'):
                handler.process_response(request, response)
