"""
Functional tests for logging users
"""

from tests.constants.constants import DefaultUser, InitUsers, InitInvalidUsers, Endpoints
from tests.functional import ApiTestBase
from tests.utils.helper import generate_full_url


class TestLogin(ApiTestBase):

    def check_status_code_200(self, status_code: int):
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")

    def test_login(self):
        """Logging users. If user got token test pass"""
        for user, password in InitUsers.users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            self.assertEqual(len(login.json().get("content")), 32, "Invalid token")

    def test_login_user_not_found(self):
        """Logging fake users. If user not found test pass"""
        for user, password in InitInvalidUsers.invalid_users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            self.assertIn("ERROR, user not found", login.text, "User founded")

    def test_login_user_locked(self):
        """Logging 3 times invalid user to lock user. If user locked test pass"""
        for user, password in InitInvalidUsers.invalid_users.items():
            for i in range(4):
                login = self.login(user, password)
                self.check_status_code_200(login.status_code)
            # print(login.text)
            self.assertIn("ERROR, user locked", login.text, "User not locked")

    def test_login_admins(self):
        """Get logged admins with admin token. If user had admin rights and got the list of logged admins test pass"""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        # print(login.text)
        token = login.json()
        token["token"] = token.pop("content")
        logged_admins = self.request_session.get(generate_full_url(Endpoints.login_admins), params=token)
        self.check_status_code_200(logged_admins.status_code)
        # print(logged_admins.text)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_admins_users(self):
        """Get logged admins without admin token. If empty response test pass"""
        for user, password in users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json()
            token["token"] = token.pop("content")
            logged_admins = self.request_session.get(generate_full_url(Endpoints.login_admins), params=token)
            self.check_status_code_200(logged_admins.status_code)
            # print(logged_admins.text)
            self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_login_users_admin(self):
        """Get logged users with admin token. If got the list of logged users test pass"""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        # print(login.text)
        token = login.json()
        token["token"] = token.pop("content")
        logged_admins = self.request_session.get(generate_full_url(Endpoints.login_users), params=token)
        self.check_status_code_200(logged_admins.status_code)
        # print(logged_admins.text)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_users(self):
        """Get logged users without admin token. If list of users empty test pass"""
        for user, password in users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json()
            token["token"] = token.pop("content")
            logged_admins = self.request_session.get(generate_full_url(Endpoints.login_users), params=token)
            self.check_status_code_200(logged_admins.status_code)
            # print(logged_admins.text)
            self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_login_tockens_admin(self):
        """Get alive tockens with admin token. If got list of tokens test pass"""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        # print(login.text)
        token = login.json()
        token["token"] = token.pop("content")
        logged_admins = self.request_session.get(generate_full_url(Endpoints.login_tockens), params=token)
        self.check_status_code_200(logged_admins.status_code)
        # print(logged_admins.text)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_tockens_users(self):
        """Get alive tockens without admin token. If list of tokens empty test pass"""
        for user, password in users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json()
            token["token"] = token.pop("content")
            logged_admins = self.request_session.get(generate_full_url(Endpoints.login_tockens), params=token)
            self.check_status_code_200(logged_admins.status_code)
            # print(logged_admins.text)
            self.assertFalse(logged_admins.json().get("content"), "Content is not empty")


users = {"akimatc": "qwerty",
         "khalaktc": "qwerty",
         "kilinatc": "qwerty",
         "OKonokhtc": "qwerty",
         "otlumtc": "qwerty",
         "slototc": "qwerty",
         "vbudktc": "qwerty",
         "vvasylystc": "qwerty"}
