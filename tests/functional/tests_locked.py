import unittest
import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser, InitUsers
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
        users = list(InitUsers.users)
        users.remove('admin')
        for user in users:
            for password in passwords:
                self.login(user, password )
        kwargs = {'token': self.adminToken }
        locked_users_request = requests.get(generate_full_url(Endpoints.locked_users), params=kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users,
                         '0 \totlumtc\n1 \tvbudktc\n2 \tvvasylystc\n3 \tkhalaktc\n4 \tslototc\n5 \tOKonokhtc\n6 \takimatc\n7 \tkilinatc\n')
        requests.get(generate_full_url(Endpoints.reset))

    def test_not_locked(self):
        """User should not be locked"""





