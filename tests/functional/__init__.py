import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request_session = requests.session()

    def login(self, name, password):
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})
