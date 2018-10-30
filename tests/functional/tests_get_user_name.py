import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestGetLoggedName(ApiTestBase):

    def test_get_user_name(self):

        # login with user
        login = self.login("slototc", "qwerty")
        token = login.json()['content']

        # get user name from response
        response = requests.get(generate_full_url(Endpoints.user), params={'token': token})
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual("slototc", returned_user_name)

    def test_get_username_with_invalid_token(self):

        """Get username with invalid token"""
        login = self.login("vvasylystc", "qwerty")
        token = login.json()['content'] + "WK"

        # get user name from response
        response = requests.get(generate_full_url(Endpoints.user), params={'token': token})
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual("vvasylystc", returned_user_name)
