"""Get user name. For getting valid response we need only token of logged in user"""
from tests.constants.constants import UserToTest
from tests.functional import ApiTestBase


class TestGetLoggedName(ApiTestBase):
    """Getting logged in name with existing user"""

    def setUp(self):
        """Get user token"""

        super().setUp()
        response = self.login(UserToTest.login, UserToTest.password)
        self.token = response.json()['content']
        self.assertEqual(200, response.status_code, "login error")

    def test_get_user_name(self):
        """Getting logged in name with existing user"""

        # get user name from response
        response = self.get_user_name(self.token)
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual(UserToTest.login, returned_user_name)

    def test_invalid_token(self):
        """Get username with invalid token"""

        wrong_token = self.token + "WK"

        # get user name from response
        response = self.get_user_name(wrong_token)
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual(UserToTest.login, returned_user_name)
