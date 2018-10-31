"""Base class and functions for testing"""

import unittest
import requests

from requests import request

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):
    """Main class for testing"""

    def setUp(self):
        """Define open request session that will be executed before each test method."""
        self.request_session = requests.session()

    def login(self, name: str, password: str) -> request:
        """Login user with name and password."""
        return self.request_session.post(generate_full_url(Endpoints.login),
                                         params={"name": name, "password": password})

    def logout(self, name: str, token: str) -> request:
        """Logout user with name and user token."""
        return self.request_session.post(generate_full_url(Endpoints.logout),
                                         params={"name": name, "token": token})

    def login_admins(self, token: str) -> request:
        """Logged admins"""
        return self.request_session.get(generate_full_url(Endpoints.login_admins),
                                        params={"token": token})

    def login_users(self, token: str) -> request:
        """Logged users"""
        return self.request_session.get(generate_full_url(Endpoints.login_users),
                                        params={"token": token})

    def login_tockens(self, token: str) -> request:
        """Alive tokens"""
        return self.request_session.get(generate_full_url(Endpoints.login_tockens),
                                        params={"token": token})

    def admins(self, token: str) -> request:
        """All admins"""
        return self.request_session.get(generate_full_url(Endpoints.admins),
                                        params={"token": token})

    def tearDown(self):
        """Define close request session and reset API data
        that will be executed after each test method."""
        self.request_session.get(generate_full_url(Endpoints.reset))
        self.request_session.close()


class Ascertains(unittest.TestCase):
    """Class for ascertains"""

    def check_status_code_200(self, status_code: int):
        """Check if response status code is valid"""
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")
