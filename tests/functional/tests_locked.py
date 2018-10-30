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

    def tearDown(self):
        """Reset api after each test"""
        requests.get(generate_full_url(Endpoints.reset))

    def test_locked(self):
        """Test  functionality of locking users"""
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        users = list(InitUsers.users)
        users.remove('admin')
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users,
                         ('0 \totlumtc\n1 \tvbudktc\n2 \tvvasylystc\n3 \tkhalaktc\n4'
                          ' \tslototc\n5 \tOKonokhtc\n6 \takimatc\n7 \tkilinatc\n'))


    def test_not_locked(self):
        """User should not be locked"""
        passwords = ['', 'password', 'qwerty']
        users = InitUsers.users
        users.pop('admin', None)
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users,'')

    def test_manual_lock(self):
        """Test  functionality of locking users by manual command"""
        users = list(InitUsers.users)
        users.remove('admin')
        user_to_lock = users[1]
        kwargs = {'token': self.adminToken, 'name': user_to_lock}
        requests.post((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)
        locked_users_request1 = self.get_locked_users(kwargs)
        locked_users = locked_users_request1.json()['content']
        s = '0 \t' + user_to_lock + '\n'
        self.assertEqual(locked_users, s)

    def test_manual_unlock(self):
        """Test  functionality of unlocking users by manual command"""
        users = list(InitUsers.users)
        users.remove('admin')
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        user_to_lock = users[3]
        for password in passwords:
            self.login(user_to_lock, password)
        kwargs = {'token': self.adminToken, 'name': user_to_lock}
        requests.put((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)
        locked_users_request = self.get_locked_users(kwargs) 
        locked_users = locked_users_request.text
        self.assertNotIn(user_to_lock, locked_users)

    def test_reset_locked(self):
        """Test  functionality of unlocking all users"""
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        users = list(InitUsers.users)
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        requests.put(generate_full_url(Endpoints.locked_reset), params=kwargs)
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_locked_admins(self):
        """Test functionality of locking admins"""
        new_user_name = 'Shtepsel'
        new_user_pass = 'qwerty'
        self.create_new_user(self.adminToken, new_user_name, new_user_pass, 'true')
        passwords = ['', 'password', 'birthday', 'petname']
        for password in passwords:
            self.login(new_user_name, password)
        kwargs = {'token': self.adminToken}
        locked_admins = self.get_locked_admins(kwargs)
        self.assertIn(new_user_name, locked_admins.text)
