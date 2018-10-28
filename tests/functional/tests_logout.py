"""
Functional tests for logout users
"""

from tests.constants.constants import InitUsers, InitInvalidUsers
from tests.functional import ApiTestBase


class TestLogout(ApiTestBase):

    def check_status_code_200(self, status_code: int):
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")

    def test_logout(self):
        """Logout users. If request true user logout and test pass"""
        for user, password in InitUsers.users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json().get("content")
            logout = self.logout(user, token)
            self.check_status_code_200(logout.status_code)
            # print(logout.text)
            self.assertTrue(logout.json().get("content"), "User not logout")

    def test_logout_fake_users(self):
        """Logout fake users. If request false user didn't logout and test pass"""
        for user, password in InitInvalidUsers.invalid_users.items():
            login = self.login(user, password)
            # print(login.text)
            self.check_status_code_200(login.status_code)
            token = login.json().get("content")
            logout = self.logout(user, token)
            self.check_status_code_200(logout.status_code)
            # print(logout.text)
            self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_locked_users(self):
        """Logout locked users. If request false user didn't logout and test pass"""
        for user, password in InitInvalidUsers.invalid_users.items():
            for i in range(3):
                login = self.login(user, password)
                self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json().get("content")
            logout = self.logout(user, token)
            self.check_status_code_200(logout.status_code)
            # print(logout.text)
            self.assertFalse(logout.json().get("content"), "User logout")
