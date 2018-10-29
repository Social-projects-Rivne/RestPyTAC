import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.request_session = requests.session()

    def login(self, name, password):
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def logout(self, name: str, token: str):
        return self.request_session.post(generate_full_url(Endpoints.logout), {"name": name, "token": token})

    def create_new_user(self, adminToken, newName, newPassword, adminRights):
        return self.request_session.post(generate_full_url(Endpoints.user),
                                         {"token": adminToken, "name": newName, "password": newPassword,
                                          "rights": adminRights})

    def change_pass(self, token, oldpassword, newpassword):
        return self.request_session.put(generate_full_url(Endpoints.user), {"token": token, "oldpassword": oldpassword,
                                                                             "newpassword": newpassword})

    def tearDown(self):
        return self.request_session.get(generate_full_url(Endpoints.reset))

