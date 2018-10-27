import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.request_session = requests.session()

    def login(self, name, password):
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def change_cool_down_time(self, token, new_value):
        return self.request_session.put(generate_full_url(Endpoints.cooldowntime),
                                        params={"token": token, "time": new_value})

    def get_cool_down_time(self):
        return self.request_session.get(generate_full_url(Endpoints.cooldowntime))