import unittest
from bson import BSON

from cos.messages import Message, Request

class TestMessage(unittest.TestCase):

        def test_setting_headers(self):
            m = Message()
            m.set_header('test-header', 'test-value')
            self.assertEqual('test-value', m.get_header('test-header'))

        def test_default_returned_for_missing_headers(self):
            m = Message()
            self.assertIsNone(m.get_header('missing'))
            self.assertEqual('default', m.get_header('missing', 'default'))

class TestRequest(unittest.TestCase):

    def test_invalid_from_bson_construction(self):
        invalid_msg = BSON.encode({})
        self.assertRaises(Exception, Request.from_bson, invalid_msg)

    def test_valid_from_bson_construction(self):
        request = {
            'headers': [],
            'method': 'method',
            'path': 'path',
            'body': {}
        }
        valid_msg = BSON.encode(request)
        r = Request.from_bson(valid_msg)
        self.assertEqual(request['headers'], r.headers)
        self.assertEqual(request['method'], r.method)
        self.assertEqual(request['path'], r.path)
        self.assertEqual(request['body'], r.body)
        
