import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url


class ApiTestBase(unittest.TestCase):

    def setUp(self):
        self.request_session = requests.session()

    def reset(self):
        return self.request_session.get(generate_full_url(Endpoints.reset))

    def login(self, name, password):
        return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})

    def get_user_items(self, user, admintoken):
        return self.request_session.get("http://localhost:8080/item/user/{name}".format(name=user), params={"token": admintoken})

    def get_user_item(self, index, user, admintoken):
        return self.request_session.get("http://localhost:8080/item/{index}/user/{name}".format(index=index, name=user), params={"token": admintoken})

    def add_item(self, index, token, item):
        return self.request_session.post("http://localhost:8080/item/{index}".format(index=index), params={"token": token, "item": item})

    def delelete_item(self, index, token):
        return self.request_session.delete("http://localhost:8080/item/{index}".format(index=index), params={"token": token})

    def update_item(self, index, token, item):
        return self.request_session.put("http://localhost:8080/item/{index}".format(index=index), params={"token": token, "item": item})

    def get_item(self, index, token):
        return self.request_session.get("http://localhost:8080/item/{index}".format(index=index), params={"token": token})
