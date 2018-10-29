import requests

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser, Endpoints
from tests.utils.helper import generate_full_url


class TestGetLoggedName(ApiTestBase):

    def test_get_user_name(self):
        #login with user
        login = self.login("slototc", "qwerty")
        token = login.json()['content']
        # get user name from response
        response = requests.get(generate_full_url(Endpoints.user), params={'token': token})
        returned_user_name = response.json()['content']
        self.assertEqual(200, response.status_code)
        self.assertEqual("slototc", returned_user_name)



