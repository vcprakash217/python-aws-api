import unittest
import Subtractor
from http import HTTPStatus

class TestSubtractor(unittest.TestCase):

    def test_lambda_handler(self):
        event = dict()
        event['httpMethod'] = 'GET'
        context = 'default'

        response = Subtractor.lambda_handler(event, context)

        self.assertEqual(response['statusCode'], HTTPStatus.METHOD_NOT_ALLOWED.value)

    def test_subtract_null_request(self):
        event = dict()
        event['httpMethod'] = 'POST'
        context = 'default'

        response = Subtractor.lambda_handler(event, context)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_null_event_body(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345

        with self.assertRaises(KeyError):
            Subtractor.subtract(event)

    def test_subtract_empty_event_body(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = ''

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_invalid_event_body(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = 'ascf'

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_no_timestamp(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"data\": [\n{ \"title\": \"Part 1\", \"values\": [0, 3, 5, 6, 2, 9] },\n{ \"title\": \"Part 2\", \"values\": [6, 3, 1, 3, 9, 4] }\n]\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_no_data(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"timestamp\": 1493758596\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_empty_data(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"timestamp\": 1493758596\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_empty_timestamp(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"timestamp\": "",\n\"data\": [\n{ \"title\": \"Part 1\", \"values\": [0, 3, 5, 6, 2, 9] },\n{ \"title\": \"Part 2\", \"values\": [6, 3, 1, 3, 9, 4] }\n]\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_invalid_data(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"timestamp\": 1236889,\n\"data\": [\n{ \"title\": \"P1\", \"values\": [0, 3, 5, 6, 2, 9] },\n{ \"title\": \"Part 2\", \"values\": [6, 3, 1, 3, 9, 4] }\n]\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)

    def test_subtract_invalid_data_alphabets(self):
        event = dict()
        event['httpMethod'] = 'POST'
        event['pathParameters'] = dict()
        event['pathParameters']['requestId'] = 12345
        event['body'] = "{\n\"timestamp\": 1236889,\n\"data\": [\n{ \"title\": \"Part 1\", \"values\": ['a', 'd', 'f'] },\n{ \"title\": \"Part 2\", \"values\": ['z', 'x', 'c'] }\n]\n}"

        response = Subtractor.subtract(event)

        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST.value)



if __name__ == '__main__':
    unittest.main()