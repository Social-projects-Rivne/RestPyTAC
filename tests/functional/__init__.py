"""Base class and functions for testing"""

import unittest

from tests.utils.application import Wrapper


class ApiTestBase(unittest.TestCase):
    """Main class for testing"""

    application = Wrapper()

    def setUp(self):
        """Define open request session that will be executed before each test method."""
        self.application.__init__()

    def tearDown(self):
        """Define close request session and reset API data
        that will be executed after each test method."""
        self.application.__del__()


class Ascertains(unittest.TestCase):
    """Class for ascertains"""

    def check_status_code_200(self, status_code: int):
        """Check if response status code is valid"""
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")
