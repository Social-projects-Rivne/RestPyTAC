import requests

from tests.constants.constants import Endpoints, DefaultUser
from tests.functional import ApiTestBase
from tests.utils.helper import generate_full_url


class TestChangePass(ApiTestBase):
    def setUp(self):
        """get admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_add_User_with_valid_data(self):
        # create user

        user = requests.post(generate_full_url(Endpoints.user),
                             params={'token': self.adminToken, "name": "testusero", "password": "qwertyqq",
                                     "rights": "false"})

        # login with new user
        login_with_new_user = requests.post(generate_full_url(Endpoints.login),
                                            params={"name": "testusero", "password": "qwertyqq"})
        token = login_with_new_user.json()['content']

        # change pass with invalid spaces
        change_pass = requests.put(generate_full_url(Endpoints.user),
                                   params={"token": token, "oldpassword": "qwertyqq", "newpassword": "qwerto  "})
        self.assertNotIn("true", change_pass.text, "error, pass was changed, and have spaces")

