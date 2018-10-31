import unittest
import requests

from urllib3 import response
from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):


    def setUp(self):
        self.request_session = requests.session()

    def login(self, name:str, password:str) -> object:
        """Login user"""
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def get_locked_users(self, kwargs):
        """Get locked users"""
        return self.request_session.get(generate_full_url(Endpoints.locked_users), params = kwargs)

    def get_locked_admins(self, kwargs):
        """Get locked admins"""
        return self.request_session.get(generate_full_url(Endpoints.locked_admins), params = kwargs)

    def get_logined_admins(self, kwargs):
        """Get logined admins"""
        return self.request_session.get(generate_full_url(Endpoints.login_admins), params = kwargs)

    def lock_user(self,user_to_lock, kwargs):
        """Lock user by manual command"""
        return self.request_session.post((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)

    def unlock_all_users(self, kwargs):
        """Unlock all users"""
        return self.request_session.put(generate_full_url(Endpoints.locked_reset), params=kwargs)

    def unlock_user(self, user_to_lock, kwargs):
        """Unlock user by manual command"""
        return self.request_session.put((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)

    def get_logined_users(self, kwargs):
        """Get logined users"""
        return self.request_session.get(generate_full_url(Endpoints.login_users), params = kwargs)

    def logout(self, name: str, token: str):
        return self.request_session.post(generate_full_url(Endpoints.logout), {"name": name, "token": token})

    def create_new_user(self, adminToken, newName, newPassword, adminRights):
        return self.request_session.post(generate_full_url(Endpoints.user),
                                         {"token": adminToken, "name": newName, "password": newPassword,
                                          "rights": adminRights})

    def tearDown(self):
        return self.request_session.get(generate_full_url(Endpoints.reset))
