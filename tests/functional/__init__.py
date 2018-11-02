"""Base class and functions for testing"""

import unittest

from tests.application.application import ApiWrapper
from tests.constants.constants import BaseUrl


class ApiTestBase(unittest.TestCase):
    """Main class for testing"""

    def setUp(self):
        """Define open request session that will be executed before each test method."""
        self.application = ApiWrapper(BaseUrl.base_url)
        self.application.reset()

    def tearDown(self):
        """Define close request session and reset API data
        that will be executed after each test method."""
        self.application.reset()
        del self.application
