import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestRemoveUser(ApiTestBase):

    def setUp(self):
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_remove_User_with_valid_data(self):
        # create test_user
        requests.post(generate_full_url(Endpoints.user), params={'token': self.adminToken, "name": "testuser",
                                                                 "password": "test  ", "rights": "false"})
        # delete test user
        remove_created_user = requests.post(generate_full_url(Endpoints.user),
                                            params={'token': self.adminToken, "name": "testuser"})
        self.assertIn("true", remove_created_user.text)

        # valid test = true
        # nsatupnyi robutu invalid with NotIn for invalid data usage
        # use invalid username
        # delete same username 2 times and more.
