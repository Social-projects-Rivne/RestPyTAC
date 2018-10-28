
import requests

from tests.constants.constants import DefaultUser, Endpoints
from tests.functional import ApiTestBase
from tests.utils.helper import generate_full_url


class TestGetUserName(ApiTestBase):

    def test_get_user_name(self):

        """login with admin"""

        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

#get logged user name

        get_name = requests.get(generate_full_url(Endpoints.user), params={'token': self.adminToken})
        logged_user_name = get_name.json()['content']
        self.assertIn(DefaultUser.user, logged_user_name)

