import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.request_session = requests.session()

    def login(self, name, password):
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def change_cool_down_time(self, admin_token, new_value):
        """Change cool down time"""
        return self.request_session.put(generate_full_url(Endpoints.cooldowntime),
                                        params={"token": admin_token, "time": new_value})

    def get_cool_down_time(self):
        """Get cool down time"""
        return self.request_session.get(generate_full_url(Endpoints.cooldowntime))

    def change_token_life_time(self, admin_token, new_value):
        """Change token life time"""
        return self.request_session.put(generate_full_url(Endpoints.tokenlifetime),
                                        params={"token": admin_token, "time": new_value})

    def get_token_life_time(self):
        """Get token life time"""
        return self.request_session.get(generate_full_url(Endpoints.tokenlifetime))

    def get_all_users(self, admin_token):
        """Get all users"""
        return self.request_session.get(generate_full_url(Endpoints.users), params={"token": admin_token})

    def tearDown(self):
        """Define close request session and reset API data
        that will be executed after each test method."""
        self.request_session.get(generate_full_url(Endpoints.reset))
        self.request_session.close()
