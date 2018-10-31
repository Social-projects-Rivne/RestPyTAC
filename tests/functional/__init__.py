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

    def create_new_user(self, admin_token, new_name, new_password, admin_rights):
        """create new user"""
        return self.request_session.post(generate_full_url(Endpoints.user),
                                         {"token": admin_token, "name": new_name, "password": new_password,
                                          "rights": admin_rights})

    def change_pass(self, token, old_password, new_password):
        """change pass"""
        return self.request_session.put(generate_full_url(Endpoints.user),
                                        {"token": token, "oldpassword": old_password,
                                         "newpassword": new_password})

    def get_user_name(self, token):
        """get user name of logged user"""
        return self.request_session.get(generate_full_url(Endpoints.user), params={"token": token})

    def delete_user(self, admin_token, name):
        """delete user"""
        return self.request_session.delete(generate_full_url(Endpoints.user), params={"token": admin_token,
                                                                                      "name": name})

    def tearDown(self):
        return self.request_session.get(generate_full_url(Endpoints.reset))

    def get_all_users(self, admin_token):
        return self.request_session.get(generate_full_url(Endpoints.users), params={"token": admin_token})
