import unittest
from cos.middleware import Repository

class BadHandler(object):
    pass


class DummyHandler(object):

    process_request_called = False
    process_response_called = False

    def process_request(self, request):
        self.process_request_called = True

    def process_response(self, request, response):
        self.process_response_called = True


class TestRespository(unittest.TestCase):

    def test_handlers_can_be_added(self):
        r = Repository()
        h = BadHandler()
        self.assertRaises(Exception, r.add_handler, h)

    def test_registered_handler_called(self):
        r = Repository()
        h = DummyHandler()
        r.add_handler(h)
        r.process_request({})
        self.assertTrue(h.process_request_called)
        r.process_response({}, {})
        self.assertTrue(h.process_response_called)

