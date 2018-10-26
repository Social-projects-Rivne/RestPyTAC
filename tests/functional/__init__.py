import unittest
import requests

from urllib3 import response
from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):


    def setUp(self):
        self.request_session = requests.session()

    def login(self, name:str, password:str) -> response:
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})
