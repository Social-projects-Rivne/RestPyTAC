from tests.functional import ApiTestBase


class TestGetLoggedName(ApiTestBase):
    """Getting logged in name with existing user"""

    def test_get_user_name(self):

        """Getting logged in name with existing user"""

        # login with user
        login = self.login("slototc", "qwerty")
        token = login.json()['content']

        # get user name from response
        response = self.get_user_name(token)
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual("slototc", returned_user_name)

    def test_invalid_token(self):
        """Get username with invalid token"""
        login = self.login("vvasylystc", "qwerty")
        token = login.json()['content'] + "WK"

        # get user name from response
        response = self.get_user_name(token)
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertNotEqual("vvasylystc", returned_user_name)
