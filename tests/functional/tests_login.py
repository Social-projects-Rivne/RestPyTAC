"""Functional tests for logging users"""

from tests.constants.constants import DefaultUser, Users, DefaultToken
from tests.functional import ApiTestBase, Ascertains


class TestLogin(ApiTestBase, Ascertains):
    """Class for testing"""

    def test_login(self):
        """Login user. If user got token test pass."""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        self.assertEqual(len(login.json().get("content")), 32, "Invalid token")

    def test_login_user_not_found(self):
        """Login fake user name. If user not found test pass."""
        login = self.login(Users.fake_user, Users.fake_password)
        self.check_status_code_200(login.status_code)
        self.assertIn("ERROR, user not found", login.text, "User founded")

    def test_login_user_locked(self):
        """Login 4 times with fake password to lock. If user locked test pass."""
        for _ in range(4):
            login = self.login(Users.valid_user, Users.fake_password)
            self.check_status_code_200(login.status_code)
        self.assertIn("ERROR, user locked", login.text, "User not locked")

    def test_login_fake_user_locked(self):
        """Login 4 times with fake user to lock. If user not found test pass."""
        for _ in range(4):
            login = self.login(Users.fake_user, Users.fake_password)
            self.check_status_code_200(login.status_code)
        self.assertIn("ERROR, user not found", login.text, "User locked")

    def test_login_admins(self):
        """Get logged admins with admin token.
        If user had admin rights and got the list of logged admins test pass."""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        logged_admins = self.login_admins(login.json().get("content"))
        self.check_status_code_200(logged_admins.status_code)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_admins_user(self):
        """Get logged admins without admin token. If empty response test pass."""
        login = self.login(Users.valid_user, Users.valid_password)
        self.check_status_code_200(login.status_code)
        logged_admins = self.login_admins(login.json().get("content"))
        self.check_status_code_200(logged_admins.status_code)
        self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_login_admins_default_token(self):
        """Get logged admins with default token. If empty response test pass."""
        logged_admins = self.login_admins(DefaultToken.token)
        self.check_status_code_200(logged_admins.status_code)
        self.assertFalse(logged_admins.json().get("content"), "Content is not empty")

    def test_login_users_admin(self):
        """Get logged users with admin token. If got the list of logged users test pass."""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        logged_admins = self.login_users(login.json().get("content"))
        self.check_status_code_200(logged_admins.status_code)
        self.assertTrue(logged_admins.json().get("content"), "Content is empty")

    def test_login_users(self):
        """Get logged users without admin token. If list of users empty test pass."""
        login = self.login(Users.valid_user, Users.valid_password)
        self.check_status_code_200(login.status_code)
        logged_users = self.login_users(login.json().get("content"))
        self.check_status_code_200(logged_users.status_code)
        self.assertFalse(logged_users.json().get("content"), "Content is not empty")

    def test_login_users_default_token(self):
        """Get logged users without admin token. If list of users empty test pass."""
        logged_users = self.login_users(DefaultToken.token)
        self.check_status_code_200(logged_users.status_code)
        self.assertFalse(logged_users.json().get("content"), "Content is not empty")

    def test_login_tockens_admin(self):
        """Get alive tockens with admin token. If got list of tokens test pass."""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        alive_tokens = self.login_tockens(login.json().get("content"))
        self.check_status_code_200(alive_tokens.status_code)
        self.assertTrue(alive_tokens.json().get("content"), "Content is empty")

    def test_login_tockens_users(self):
        """Get alive tockens without admin token. If list of tokens empty test pass"""
        login = self.login(Users.valid_user, Users.valid_password)
        self.check_status_code_200(login.status_code)
        alive_tokens = self.login_tockens(login.json().get("content"))
        self.check_status_code_200(alive_tokens.status_code)
        self.assertFalse(alive_tokens.json().get("content"), "Content is not empty")

    def test_login_tockens_users_default_token(self):
        """Get alive tockens with default token. If list of tokens empty test pass"""
        alive_tokens = self.login_tockens(DefaultToken.token)
        self.check_status_code_200(alive_tokens.status_code)
        self.assertFalse(alive_tokens.json().get("content"), "Content is not empty")
