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

    def get_locked_admins(self, kwargs):
        return self.request_session.get(generate_full_url(Endpoints.locked_admins), params = kwargs)

    def get_logined_admins(self, kwargs):
        return self.request_session.get(generate_full_url(Endpoints.login_admins), params = kwargs)

    def get_logined_users(self, kwargs):
        return self.request_session.get(generate_full_url(Endpoints.login_users), params = kwargs)

    def logout(self, name: str, token: str):
        return self.request_session.post(generate_full_url(Endpoints.logout), {"name": name, "token": token})

    def create_new_user(self, adminToken, newName, newPassword, adminRights):
        return self.request_session.post(generate_full_url(Endpoints.user),
                                         {"token": adminToken, "name": newName, "password": newPassword,
                                          "rights": adminRights})

    def tearDown(self):
        return self.request_session.get(generate_full_url(Endpoints.reset))
