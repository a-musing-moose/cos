import unittest

from cos.messages import Request, ErrorResponse
from cos.views import View

class TestView(unittest.TestCase):

    def test_that_dispatch_errors(self):
        v = View()
        self.assertRaises(ErrorResponse, v.dispatch, Request())
