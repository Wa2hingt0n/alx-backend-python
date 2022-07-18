#!/usr/bin/env python3
""" Defines a test class 'TestAccessNestaedMap' """
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Any, Union
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Creates a parameterized test for the utils.access_nested_map method """
    @parameterized.expand([
        ("not_nested", {"a": 1}, ("a",), 1),
        ("nested_idx_0", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("nested_value", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            name: str, nested_map: Dict,
            path: Tuple[str],
            expected: Union[int, Dict]) -> None:
        """ Tests the 'utils.access_nested_map method' """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Exception) -> None:
        """ Tests whether a key error is raised """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJSON(unittest.TestCase):
    """ Creates a test suite for the utils.get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Test case for the utils.get_json method. Creates a mock object
        for 'requests.get' and returns a test payload """
        kwargs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**kwargs)) as mock_req:
            self.assertEqual(get_json(test_url), test_payload)
            mock_req.assert_called_once_with(test_url)
