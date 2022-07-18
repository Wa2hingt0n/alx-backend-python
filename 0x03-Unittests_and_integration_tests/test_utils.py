#!/usr/bin/env python3
""" Defines a test class 'TestAccessNestaedMap' """
import unittest
from typing import Dict, Tuple, Any, Union
from parameterized import parameterized
from utils import access_nested_map


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
