import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestCreateNewUser(ApiTestBase):

    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_add_User_with_valid_data(self):

        """login and get admin token"""

        create_user = requests.post(generate_full_url(Endpoints.user),
                                    params={'token': self.adminToken, "name": "validtest",
                                            "password": "qwertyqq", "rights": "true"})
        self.assertIn("true", create_user.text)
