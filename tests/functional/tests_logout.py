"""Functional tests for logout users"""

from tests.constants.constants import DefaultUser, Users, DefaultToken, VALID_STATUS_CODE
from tests.functional import ApiTestBase


class TestLogout(ApiTestBase):
    """Class for testing"""

    def test_logout(self):
        """Logout user. If request true and user logout test pass."""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(DefaultUser.user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertTrue(logout.json().get("content"), "User not logout")

    def test_logout_another_user(self):
        """Login user1, logout another user2 with user1 token.
        If request false and user2 didn't logout test pass."""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.valid_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_another_token(self):
        """Login user, logout with another token.
        If request false and user didn't logout test pass."""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(DefaultUser.user, DefaultToken.token)
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_fake_users(self):
        """Logout fake user. If request false and user didn't logout test pass."""
        login = self.application.login(Users.fake_user, Users.fake_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.fake_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")

    def test_logout_locked_users(self):
        """Logout locked user. If request false user didn't logout and test pass."""
        for _ in range(4):
            login = self.application.login(Users.valid_user, Users.fake_password)
            self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logout = self.application.logout(Users.fake_user, login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logout.status_code)
        self.assertFalse(logout.json().get("content"), "User logout")
