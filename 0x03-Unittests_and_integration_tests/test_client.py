#!/usr/bin/env python3
""" Defines a test suite """
import requests
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import Mock, patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Creates a Test suite for the 'GithubOrgClient' class """
    @parameterized.expand([
        ("google", {"name": "google"}),
        ("abc", {"name": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict,  mock_fn: MagicMock) -> None:
        """ Tests the 'client.GithuborgClient.org' method """
        mock_fn.return_value = MagicMock(return_value=response)
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org(), response)
        url = "https://api.github.com/orgs/{}".format(org)
        mock_fn.assert_called_once_with(url)
