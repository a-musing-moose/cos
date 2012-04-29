class NullCodex():
    """
    empty codex that doesn't actually do anything
    """

    def decode_request(self, request):
        """
        Decodes the request object
        """
        pass

    def encode_response(self, response):
        """
        Encodes the response object
        """
        pass

class Auth():
    """
    The auth module is responsible for authenticating the request
    and assigning the correct user to the request context
    """

    def get_application(request):
        pass

class SecurityMiddleWare()):
    """
    Middleware handler for security. This one just uses
    the NullCodex by default but could be extended tu use
    and codex you wish
    """
    
    codex = NullCodex()
    auth = Auth()

    def process_request(self, request):
        """
        Processes the incoming request
        decoding and authenticating
        """
        self.codex.decode_request(request)
        application = self.auth.get_application(request)
        request.context['application'] = application

    def process_response(self, request, response):
        """
        Processes the outgoing response
        """
        self.codex.encode_response(response)
