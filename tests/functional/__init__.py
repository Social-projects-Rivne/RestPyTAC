import unittest
import requests

from urllib3 import response
from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):


    def setUp(self):
        self.request_session = requests.session()

    def login(self, name:str, password:str) -> object:
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def get_locked_users(self, kwargs):
        return self.request_session.get(generate_full_url(Endpoints.locked_users), params = kwargs)

    def get_logined_users(self, kwargs):
        return self.request_session.get(generate_full_url(Endpoints.login_users), params = kwargs)
