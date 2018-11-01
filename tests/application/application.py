import requests
from requests import request

from tests.constants.constants import Endpoints


class ApiWrapper:

    def __init__(self, app_url):
        self.request_session = requests.session()
        self.base_url = app_url

    def __del__(self):
        self.request_session.close()

    def _generate_full_url(self, path):
        """Generate the full url with base url and path"""
        return "{}{}".format(self.base_url, path)

    def reset(self):
        """Reset API"""
        return self.request_session.get(self._generate_full_url(Endpoints.reset))

    def login(self, name: str, password: str) -> request:
        """Login user with name and password."""
        return self.request_session.post(self._generate_full_url(Endpoints.login),
                                         params={"name": name, "password": password})

    def logout(self, name: str, token: str) -> request:
        """Logout user with name and user token."""
        return self.request_session.post(self._generate_full_url(Endpoints.logout),
                                         params={"name": name, "token": token})

    def login_admins(self, token: str) -> request:
        """Logged admins"""
        return self.request_session.get(self._generate_full_url(Endpoints.login_admins),
                                        params={"token": token})

    def login_users(self, token: str) -> request:
        """Logged users"""
        return self.request_session.get(self._generate_full_url(Endpoints.login_users),
                                        params={"token": token})

    def login_tockens(self, token: str) -> request:
        """Alive tokens"""
        return self.request_session.get(self._generate_full_url(Endpoints.login_tockens),
                                        params={"token": token})

    def admins(self, token: str) -> request:
        """All admins"""
        return self.request_session.get(self._generate_full_url(Endpoints.admins),
                                        params={"token": token})

    def get_user_all_items(self, user, admin_token):
        """Get all user items"""
        return self.request_session.get(self._generate_full_url(Endpoints.item_user).format(name=user),
                                        params={"token": admin_token})

    def get_user_item_by_index(self, index, user, admin_token):
        """Get user item by index"""
        return self.request_session.get(self._generate_full_url(Endpoints.item_user_by_index).format(index=index,
                                                                                                     name=user),
                                        params={"token": admin_token})

    def add_item(self, index, token, item):
        """Add item"""
        return self.request_session.post(self._generate_full_url(Endpoints.item).format(index=index),
                                         params={"token": token, "item": item})

    def delete_item(self, index, token):
        """Delete item"""
        return self.request_session.delete(self._generate_full_url(Endpoints.item).format(index=index),
                                           params={"token": token})

    def update_item(self, index, token, item):
        """Update item"""
        return self.request_session.put(self._generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token, "item": item})

    def get_item(self, index, token):
        """Get item by index"""
        return self.request_session.get(self._generate_full_url(Endpoints.item).format(index=index),
                                        params={"token": token})

    def get_item_indexes(self, token):
        """Get all item indexes"""
        return self.request_session.get(self._generate_full_url(Endpoints.itemindexes), params={"token": token})

    def get_all_items(self, token):
        """Get all items by user"""
        return self.request_session.get(self._generate_full_url(Endpoints.items), params={"token": token})

    def change_cool_down_time(self, admin_token, new_value):
        """Change cool down time"""
        return self.request_session.put(self._generate_full_url(Endpoints.cooldowntime),
                                        params={"token": admin_token, "time": new_value})

    def get_cool_down_time(self):
        """Get cool down time"""
        return self.request_session.get(self._generate_full_url(Endpoints.cooldowntime))

    def change_token_life_time(self, admin_token, new_value):
        """Change token life time"""
        return self.request_session.put(self._generate_full_url(Endpoints.tokenlifetime),
                                        params={"token": admin_token, "time": new_value})

    def get_token_life_time(self):
        """Get token life time"""
        return self.request_session.get(self._generate_full_url(Endpoints.tokenlifetime))

    def get_all_users(self, admin_token):
        """Get all users"""
        return self.request_session.get(self._generate_full_url(Endpoints.users), params={"token": admin_token})

    def get_locked_users(self, admin_token):
        """Get locked users"""
        return self.request_session.get(self._generate_full_url(Endpoints.locked_users),
                                        params={"token": admin_token})

    def get_locked_admins(self, admin_token):
        """Get locked admins"""
        return self.request_session.get(self._generate_full_url(Endpoints.locked_admins),
                                        params={"token": admin_token})

    def lock_user(self, admin_token, user_to_lock):
        """Lock user by manual command"""
        return self.request_session.post((self._generate_full_url(Endpoints.locked_user) + user_to_lock),
                                         params={"token": admin_token, 'name': user_to_lock})

    def unlock_all_users(self, admin_token):
        """Unlock all users"""
        return self.request_session.put(self._generate_full_url(Endpoints.locked_reset),
                                        params={"token": admin_token})

    def unlock_user(self, admin_token, user_to_unlock):
        """Unlock user by manual command"""
        return self.request_session.put((self._generate_full_url(Endpoints.locked_user) + user_to_unlock),
                                        params={"token": admin_token, 'name': user_to_unlock})

    def create_new_user(self, admin_token, new_name, new_password, admin_rights):
        """Create new user"""
        return self.request_session.post(self._generate_full_url(Endpoints.user),
                                         {"token": admin_token, "name": new_name,
                                          "password": new_password,
                                          "rights": admin_rights})

    def change_pass(self, token, old_password, new_password):
        """change pass"""
        return self.request_session.put(self._generate_full_url(Endpoints.user), {"token": token,
                                                                                  "oldpassword": old_password,
                                                                                  "newpassword": new_password})

    def get_user_name(self, token):
        """get user name of logged user"""
        return self.request_session.get(self._generate_full_url(Endpoints.user), params={"token": token})

    def delete_user(self, admin_token, name):
        """delete user"""
        return self.request_session.delete(self._generate_full_url(Endpoints.user), params={"token": admin_token,
                                                                                            "name": name})
