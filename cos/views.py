from messages import Response, ErrorResponse
from resources import Resource


class View(object):
    """
    Intentionally simple parent class for all views. Only implements
    dispatch-by-method and simple sanity checking.
    """

    permitted_methods = ()

    def dispatch(self, request):
        """
        Try to dispatch to the right method; if a method doesn't exist,
        defer to the error handler. Also defer to the error handler if the
        request method isn't on the approved list.
        """
        handler = self._method_not_allowed
        method = request.method.lower()
        if method in self.permitted_methods and hasattr(self, method):
            handler = getattr(self, method)
        return handler(request.body)

    def _method_not_allowed(self, request):
        """
        Simple handler for disallowed methods
        """
        raise ErrorResponse("method not allowed")


class ResourceMixin():
    """
    Base mixin for resources. Handles the basic CRUD operations.
    """
    permitted_methods = ('create', 'update', 'delete', 'find')

    resource = None

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, data):
        pass

    def find(self, data):
        pass

    def _get_resource(self):
        if self.resource:
            return self.resource
        else:
            return Resource


class ResourceView(ResourceMixin, View):
    """
    Unadorned view for resources.
    """
    pass
