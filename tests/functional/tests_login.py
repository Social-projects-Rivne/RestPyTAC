"""Functional tests for logging users"""

from ddt import data, ddt

from tests.constants.constants import DefaultToken, DefaultUser, Users, VALID_STATUS_CODE
from tests.functional import ApiTestBase


@ddt
class TestLogin(ApiTestBase):
    """Class for testing"""

    def test_login(self):
        """Login user. If user got token test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        self.assertEqual(len(login.json().get("content")), 32, "Invalid token")

    def test_login_user_not_found(self):
        """Login fake user name. If user not found test pass (negative)"""
        login = self.application.login(Users.fake_user, Users.fake_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        self.assertIn("ERROR, user not found", login.text, "User founded")

    def test_login_user_locked(self):
        """Login 4 times with valid user and fake password to lock. If user locked test pass (negative)"""
        for _ in range(4):
            login = self.application.login(Users.valid_user, Users.fake_password)
            self.assertEqual(VALID_STATUS_CODE, login.status_code)
        self.assertIn("ERROR, user locked", login.text, "User not locked")

    def test_login_fake_user_locked(self):
        """Login 4 times with fake user and password to lock. If user not found test pass (negative)"""
        for _ in range(4):
            login = self.application.login(Users.fake_user, Users.fake_password)
            self.assertEqual(VALID_STATUS_CODE, login.status_code)
        self.assertIn("ERROR, user not found", login.text, "User locked")

    def test_login_admins(self):
        """Get logged admins with admin token. If got the list of logged admins test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logged_admins = self.application.login_admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_admins_user(self):
        """Get logged admins with user token. If empty response test pass (positive)"""
        login = self.application.login(Users.valid_user, Users.valid_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logged_admins = self.application.login_admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    @data(DefaultToken.token, "")
    def test_login_admins_token(self, value):
        """Get logged admins with default and empty token. If empty response test pass (negative)"""
        logged_admins = self.application.login_admins(value)
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_login_users_admin(self):
        """Get logged users with admin token. If got the list of logged users test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logged_admins = self.application.login_users(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_admins.status_code)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_users(self):
        """Get logged users with user token. If list of users empty test pass (negative)"""
        login = self.application.login(Users.valid_user, Users.valid_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        logged_users = self.application.login_users(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, logged_users.status_code)
        self.assertFalse(logged_users.json().get("content"), "Content is not empty")

    @data(DefaultToken.token, "")
    def test_login_users_token(self, value):
        """Get logged users with default and empty token. If list of users empty test pass (negative)"""
        logged_users = self.application.login_users(value)
        self.assertEqual(VALID_STATUS_CODE, logged_users.status_code)
        self.assertFalse(logged_users.json().get("content"), "Content is not empty")

    def test_login_tockens_admin(self):
        """Get alive tockens with admin token. If got list of tokens test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        alive_tokens = self.application.login_tockens(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, alive_tokens.status_code)
        self.assertTrue(alive_tokens.json().get("content"), "Content is empty")

    def test_login_tockens_users(self):
        """Get alive tockens with user token. If list of tokens empty test pass (negative)"""
        login = self.application.login(Users.valid_user, Users.valid_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        alive_tokens = self.application.login_tockens(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, alive_tokens.status_code)
        self.assertFalse(alive_tokens.json().get("content"), "Content is not empty")

    @data(DefaultToken.token, "")
    def test_login_tockens_users_token(self, value):
        """Get alive tockens with default and empty token. If list of tokens empty test pass (negative)"""
        alive_tokens = self.application.login_tockens(value)
        self.assertEqual(VALID_STATUS_CODE, alive_tokens.status_code)
        self.assertFalse(alive_tokens.json().get("content"), "Content is not empty")
