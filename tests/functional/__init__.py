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

    def get_user_all_items(self, user, admintoken):
        return self.request_session.get(generate_full_url(Endpoints.item_user).format(name=user),
                                        params={"token": admintoken})

    def get_user_item_by_index(self, index, user, admintoken):
        return self.request_session.get(generate_full_url(Endpoints.item_user_by_index).format(index=index, name=user),
                                        params={"token": admintoken})

    def add_item(self, index, token, item):
        return self.request_session.post(generate_full_url(Endpoints.item).format(index=index),
                                         params={"token": token, "item": item})

    def delete_item(self, index, token):
        return self.request_session.delete(generate_full_url(Endpoints.item).format(index=index),
                                           params={"token": token})

    def update_item(self, index, token, item):
        return self.request_session.put(generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token, "item": item})

    def get_item(self, index, token):
        return self.request_session.get(generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token})

    def get_itemindexes(self, token):
        return self.request_session.get(generate_full_url(Endpoints.itemindexes), params={"token": token})

    def get_all_items(self, token):
        return self.request_session.get(generate_full_url(Endpoints.items), params={"token": token})
