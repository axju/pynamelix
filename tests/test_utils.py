import json
import pathlib
import unittest
from unittest import mock

from pynamelix.utils import get_names


class MockResponse:
    def __init__(self, json_data_file, status_code):
        with json_data_file.open('r') as json_file:
            self.json_data = json.load(json_file)
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_get_names(*args, **kwargs):
    root = pathlib.Path(__file__)
    json_data_file = root.parent / 'data.json'
    return MockResponse(json_data_file, 200)


class TestGetNames(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_get_names)
    def test_get_names(self, mock_get):
        names = list(get_names('test'))
        self.assertIsInstance(names, list)
        self.assertEqual(len(names), 80)
