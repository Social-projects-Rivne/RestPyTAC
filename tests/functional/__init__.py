"""Base class and functions for testing"""

import unittest

from tests.application.application import ApiWrapper
from tests.constants.constants import BaseUrl


class ApiTestBase(unittest.TestCase):
    """Main class for testing"""

    @classmethod
    def setUpClass(cls):
        """Define open request session that will be executed before each class test method."""
        cls.application = ApiWrapper(BaseUrl.base_url)

    def setUp(self):
        """Define reset API data before each test method."""
        self.application.reset()

    def tearDown(self):
        """Reset API data that will be executed after each test method."""
        self.application.reset()


class Assertions(unittest.TestCase):
    """Class for Assertions"""

    def check_status_code_200(self, status_code: int):
        """Check if response status code is valid"""
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")
