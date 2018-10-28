import unittest

import requests

from tests.constants.constants import Endpoints, DefaultUser
from tests.functional import ApiTestBase
from tests.utils.helper import generate_full_url


class TestChangePass(ApiTestBase):


    def test_change_pass(self):

        """login as user and get token. Do it after creating user"""

        response = self.login("qwert", "qwertyqq")
        self.token = response.json()['content']

        """Create new user"""

        change_pass = requests.put(generate_full_url(Endpoints.user),
                                    params=dict(token=self.token, oldpassword="qwertyqq", newpassword="qwertyqq"))

        self.assertIn("true", change_pass.text,"continue./ all is good")

# add spaces in newpassword. but be carefully. it's will change pass in login, and change_pass
# if true = it's mean pass sucsessfully changed. but it's error!
        wrong_change_pass = requests.put(generate_full_url(Endpoints.user),
                                   params={'token': self.token, 'oldpassword':"qwertyqq", 'newpassword':"qwertyqq"})

        self.assertNotIn("True", str(wrong_change_pass.json()['content']), "Error! pass was created with spaces")


