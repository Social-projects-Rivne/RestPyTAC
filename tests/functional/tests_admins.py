"""Functional tests for admins"""

from tests.constants.constants import Users, DefaultUser, DefaultToken
from tests.functional import ApiTestBase, Assertions


class TestAdmins(ApiTestBase, Assertions):
    """Class for testing"""

    def test_admins(self):
        """Get all admins with admin token. If list not empty test pass."""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        all_admins = self.admins(login.json().get("content"))
        self.check_status_code_200(all_admins.status_code)
        self.assertTrue(all_admins.json().get("content"), "Content is empty")

    def test_admins_user(self):
        """Get all admins without admin token. If list empty test pass"""
        login = self.login(Users.valid_user, Users.valid_password)
        self.check_status_code_200(login.status_code)
        all_admins = self.admins(login.json().get("content"))
        self.check_status_code_200(all_admins.status_code)
        self.assertFalse(all_admins.json().get("content"), "Content is not empty")

    def test_admins_default_token(self):
        """Get all admins with default token. If list empty test pass"""
        all_admins = self.admins(DefaultToken.token)
        self.check_status_code_200(all_admins.status_code)
        self.assertFalse(all_admins.json().get("content"), "Content is not empty")
