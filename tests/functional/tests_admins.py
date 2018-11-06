"""Functional tests for admins"""

from ddt import data, ddt

from tests.constants.constants import DefaultToken, DefaultUser, Users, VALID_STATUS_CODE
from tests.functional import ApiTestBase


@ddt
class TestAdmins(ApiTestBase):
    """Class for testing"""

    def test_admins(self):
        """Get all admins with admin token. If list not empty test pass (positive)"""
        login = self.application.login(DefaultUser.user, DefaultUser.password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        all_admins = self.application.admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, all_admins.status_code)
        self.assertTrue(all_admins.json().get("content"), "Content is empty")

    def test_admins_user(self):
        """Get all admins with user token. If list empty test pass (negative)"""
        login = self.application.login(Users.valid_user, Users.valid_password)
        self.assertEqual(VALID_STATUS_CODE, login.status_code)
        all_admins = self.application.admins(login.json().get("content"))
        self.assertEqual(VALID_STATUS_CODE, all_admins.status_code)
        self.assertFalse(all_admins.json().get("content"), "Content is not empty")

    @data(DefaultToken.token, "")
    def test_admins_token(self, value):
        """Get all admins with default and empty token. If list empty test pass (negative)"""
        all_admins = self.application.admins(value)
        self.assertEqual(VALID_STATUS_CODE, all_admins.status_code)
        self.assertFalse(all_admins.json().get("content"), "Content is not empty")
