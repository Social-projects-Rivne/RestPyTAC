import unittest
import requests

from requests import request

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.request_session = requests.session()

    def login(self, name: str, password: str) -> request:
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def logout(self, name: str, token: str) -> request:
        return self.request_session.post(generate_full_url(Endpoints.logout), {"name": name, "token": token})

    def tearDown(self):
        self.request_session.get(generate_full_url(Endpoints.reset))
        self.request_session.close()
