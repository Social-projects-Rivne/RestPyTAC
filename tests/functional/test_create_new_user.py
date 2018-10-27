import unittest
import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestLocked(ApiTestBase):

    def test_add_User(self):

        """login and get admin token"""

        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

        """create new user with admin token, and with rights: ADMIN """

        create_user = requests.post(generate_full_url(Endpoints.user),
                                    params={'token': self.adminToken, "name": "qwert",
                                            "password": "qwertyqq", "rights": "true"})
        self.assertIn("true", create_user.text)
