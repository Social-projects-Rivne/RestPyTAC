import unittest
import requests

from tests.constants.constants import Endpoints
from tests.utils.helper import generate_full_url
from requests import request


class ApiTestBase(unittest.TestCase):
    """Main class for testing"""

    def setUp(self):
        """Define open request session that will be executed before each test method."""
        self.request_session = requests.session()

    def reset(self):
        """Reset API"""
        return self.request_session.get(generate_full_url(Endpoints.reset))

    def login(self, name: str, password: str) -> request:
        """Login user with name and password."""
        return self.request_session.post(generate_full_url(Endpoints.login),
                                         params={"name": name, "password": password})

    def logout(self, name: str, token: str) -> request:
        """Logout user with name and user token."""
        return self.request_session.post(generate_full_url(Endpoints.logout),
                                         params={"name": name, "token": token})

    def login_admins(self, token: str) -> request:
        """Logged admins"""
        return self.request_session.get(generate_full_url(Endpoints.login_admins),
                                        params={"token": token})

    def login_users(self, token: str) -> request:
        """Logged users"""
        return self.request_session.get(generate_full_url(Endpoints.login_users),
                                        params={"token": token})

    def login_tockens(self, token: str) -> request:
        """Alive tokens"""
        return self.request_session.get(generate_full_url(Endpoints.login_tockens),
                                        params={"token": token})

    def admins(self, token: str) -> request:
        """All admins"""
        return self.request_session.get(generate_full_url(Endpoints.admins),
                                        params={"token": token})

    def get_user_all_items(self, user, admin_token):
        """Get all user items"""
        return self.request_session.get(generate_full_url(Endpoints.item_user).format(name=user),
                                        params={"token": admin_token})

    def get_user_item_by_index(self, index, user, admin_token):
        """Get user item by index"""
        return self.request_session.get(generate_full_url(Endpoints.item_user_by_index).format(index=index, name=user),
                                        params={"token": admin_token})

    def add_item(self, index, token, item):
        """Add item"""
        return self.request_session.post(generate_full_url(Endpoints.item).format(index=index),
                                         params={"token": token, "item": item})

    def delete_item(self, index, token):
        """Delete item"""
        return self.request_session.delete(generate_full_url(Endpoints.item).format(index=index),
                                           params={"token": token})

    def update_item(self, index, token, item):
        """Update item"""
        return self.request_session.put(generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token, "item": item})

    def get_item(self, index, token):
        """Get item by index"""
        return self.request_session.get(generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token})

    def get_item_indexes(self, token):
        """Get all item indexes"""
        return self.request_session.get(generate_full_url(Endpoints.itemindexes), params={"token": token})

    def get_all_items(self, token):
        """Get all items by user"""
        return self.request_session.get(generate_full_url(Endpoints.items), params={"token": token})

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

    def get_locked_users(self, kwargs):
            """Get locked users"""
            return self.request_session.get(generate_full_url(Endpoints.locked_users), params = kwargs)

    def get_locked_admins(self, kwargs):
        """Get locked admins"""
        return self.request_session.get(generate_full_url(Endpoints.locked_admins), params = kwargs)

    def lock_user(self, user_to_lock, admin_token):
        """Lock user by manual command"""
        return self.request_session.post((generate_full_url(Endpoints.locked_user) + user_to_lock),
                                         params= {"token": admin_token})

    def unlock_all_users(self, kwargs):
        """Unlock all users"""
        return self.request_session.put(generate_full_url(Endpoints.locked_reset),
                                        params= {"token": admin_token})

    def unlock_user(self, user_to_lock, kwargs):
        """Unlock user by manual command"""
        return self.request_session.put((generate_full_url(Endpoints.locked_user) + user_to_lock),
                                        params=kwargs)

    def tearDown(self):
        """Define close request session and reset API data
        that will be executed after each test method."""
        self.request_session.get(generate_full_url(Endpoints.reset))
        self.request_session.close()


class Ascertains(unittest.TestCase):
    """Class for ascertains"""

    def check_status_code_200(self, status_code: int):
        """Check if response status code is valid"""
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")



# import unittest
# import requests
#
# from urllib3 import response
# from tests.constants.constants import Endpoints
# from tests.utils.helper import generate_full_url
#
#
# class ApiTestBase(unittest.TestCase):
#
#
#     def setUp(self):
#         self.request_session = requests.session()
#
#     def login(self, name:str, password:str) -> object:
#         """Login user"""
#         return self.request_session.post(generate_full_url(Endpoints.login), {"name": name, "password": password})
#
#     def get_locked_users(self, kwargs):
#         """Get locked users"""
#         return self.request_session.get(generate_full_url(Endpoints.locked_users), params = kwargs)
#
#     def get_locked_admins(self, kwargs):
#         """Get locked admins"""
#         return self.request_session.get(generate_full_url(Endpoints.locked_admins), params = kwargs)
#
#     def get_logined_admins(self, kwargs):
#         """Get logined admins"""
#         return self.request_session.get(generate_full_url(Endpoints.login_admins), params = kwargs)
#
#     def lock_user(self,user_to_lock, kwargs):
#         """Lock user by manual command"""
#         return self.request_session.post((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)
#
#     def unlock_all_users(self, kwargs):
#         """Unlock all users"""
#         return self.request_session.put(generate_full_url(Endpoints.locked_reset), params=kwargs)
#
#     def unlock_user(self, user_to_lock, kwargs):
#         """Unlock user by manual command"""
#         return self.request_session.put((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)
#
#     def get_logined_users(self, kwargs):
#         """Get logined users"""
#         return self.request_session.get(generate_full_url(Endpoints.login_users), params = kwargs)
#
#     def logout(self, name: str, token: str):
#         return self.request_session.post(generate_full_url(Endpoints.logout), {"name": name, "token": token})
#
#     def create_new_user(self, adminToken, newName, newPassword, adminRights):
#         return self.request_session.post(generate_full_url(Endpoints.user),
#                                          {"token": adminToken, "name": newName, "password": newPassword,
#                                           "rights": adminRights})
#
#     def tearDown(self):
#         return self.request_session.get(generate_full_url(Endpoints.reset))
