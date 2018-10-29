import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestCreateNewUserWithInvalidName(ApiTestBase):

    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_create_User_with_invalid_username(self):
        """creating user with spaces"""
        create_user_vith_invalid_pass = requests.post(generate_full_url(Endpoints.user),
                                    params={'token': self.adminToken, "name": "invalidtestname  ",
                                            "password": "test  ", "rights": "false"})
        self.assertNotIn('true', create_user_vith_invalid_pass.text, "error, username have spaces")
