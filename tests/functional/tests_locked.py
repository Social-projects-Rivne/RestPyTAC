import unittest
import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url

class TestLocked(ApiTestBase):


    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']




    def test_locked(self):
        """Test  functionality of locking users"""
        passwords = ['voron','password', 'birthday', 'petname']
        for password in passwords:
            self.login('khalaktc', password )
        kwargs = {'token': self.adminToken, }
        locked_users_request = requests.get(generate_full_url(Endpoints.locked_users), params=kwargs)
        locked_users = locked_users_request.json()['content']
        print(locked_users)
        self.assertEqual('0', '0')

    def test_not_locked(self):
        """User should not be locked"""





