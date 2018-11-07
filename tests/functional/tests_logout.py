"""Functional tests for logout users"""

from tests.constants.constants import DefaultToken, DefaultUser, Users, VALID_STATUS_CODE
from tests.functional import ApiTestBase


class TestLogout(ApiTestBase):
    """Class for testing"""

    def test_logout(self):
        """Logout user. If request true test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logged_admins = self.application.login_admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")
        logout = self.application.logout(DefaultUser.user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertTrue(logout.json().get("content"), "User not logout")
        logged_admins = self.application.login_admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_double_logout(self):
        """Double logout user. If request true than false test pass (negative)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout1 = self.application.logout(DefaultUser.user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout1.status_code)
        self.assertTrue(logout1.json().get("content"), "User not logout")
        logout2 = self.application.logout(DefaultUser.user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout2.status_code)
        self.assertFalse(logout2.json().get("content"), "User not logout")

    def test_logout_another_user(self):
        """Login user1, logout another user2 with user1 token. If user2 didn't logout test pass (negative)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.valid_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_another_token(self):
        """Login user, logout with another token. If user didn't logout test pass (negative)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(DefaultUser.user, DefaultToken.token)
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_fake_users(self):
        """Logout fake user. If user didn't logout test pass (negative)"""
        login = self.application.login(Users.fake_user, Users.fake_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.fake_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_locked_users(self):
        """Logout locked user. If user didn't logout and test pass (negative)"""
        for _ in range(4):
            login = self.application.login(Users.valid_user, Users.fake_password)
            self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.fake_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")
