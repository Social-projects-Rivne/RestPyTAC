"""Testing functionality of locking users"""

import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser, InitUsers, InitFake
from tests.utils.helper import generate_full_url
from random import choice


class TestLocked(ApiTestBase):
    """Testing functionality of locking users"""

    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.admin_token = response.json()['content']
        self.kwargs = {'token': self.admin_token}

    def tearDown(self):
        """Reset api after each test"""
        requests.get(generate_full_url(Endpoints.reset))

    def test_locked(self):
        """Test  functionality of locking users"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user = choice(list(users.keys())) # returning random user
        wrong_password = InitFake.wrong_password
        for _ in range(3):
            self.login(user, wrong_password)
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertIn(user, locked_users)

    def test_not_locked(self):
        """User should not be locked"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user = choice(list(users.keys()))  # returning random user
        wrong_passwords = ['', 'password']
        for wrong_password in wrong_passwords:
                self.login(user, wrong_password)
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertNotIn(user, locked_users)

    def test_manual_lock(self):
        """Test  functionality of locking users by manual command"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user_to_lock = choice(list(users.keys()))  # returning random user
        self.kwargs['name'] = user_to_lock
        self.lock_user(user_to_lock, self.kwargs)
        locked_users_request1 = self.get_locked_users(self.kwargs)
        self.assertIn(user_to_lock, locked_users_request1.text)

    def test_manual_unlock(self):
        """Test  functionality of unlocking users by manual command"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user_to_lock = choice(list(users.keys()))  # returning random user
        wrong_password = InitFake.wrong_password
        for _ in range(3):
            self.login(user_to_lock, wrong_password)
        self.kwargs['name'] = user_to_lock
        self.unlock_user(user_to_lock, self.kwargs)
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.text
        self.assertNotIn(user_to_lock, locked_users)

    def test_reset_locked_admin_token(self):
        """Test  functionality of unlocking all users with admin token"""
        # passwords = ['', 'password', 'birthday']  # number of passwords determines login attemps
        users = InitUsers.users.copy()
        users.pop('admin', None)
        wrong_password = InitFake.wrong_password
        for user in users.keys():
            self.login(user, wrong_password)
        self.unlock_all_users(self.kwargs)
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_reset_locked_user_token(self):
        """Test  functionality of unlocking all users with user token"""
        pass

    def test_reset_locked_empty_token(self):
        """Test  functionality of unlocking all users with empty token"""
        pass

    def test_locked_admins(self):
        """Test functionality of locking admins"""
        new_user_name = 'Shtepsel'
        new_user_pass = 'qwerty'
        self.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        passwords = ['', 'password', 'birthday', 'petname']
        for password in passwords:
            self.login(new_user_name, password)
        kwargs = {'token': self.admin_token}
        locked_admins = self.get_locked_admins(kwargs)
        self.assertIn(new_user_name, locked_admins.text)

    def test_not_locked_admin(self):
        """Admin should not be locked"""
        new_user_name = 'Shtepsel'
        new_user_pass = 'qwerty'
        self.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        passwords = ['', 'password', 'qwerty']
        for password in passwords:
            self.login(new_user_name, password)
        kwargs = {'token': self.admin_token}
        locked_admins = self.get_locked_admins(kwargs)
        logined_admins = self.get_logined_admins(kwargs)
        self.assertNotIn(new_user_name, locked_admins.text)
        self.assertIn(new_user_name, logined_admins.text)

    def test_manual_lock_user_token(self):
        """Test  functionality of locking users by manual command with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user_to_lock = list(users.keys())[1]
        tokens = []
        for user, password in users.items():
            login_for_token = self.login(user, password)
            tokens.append(login_for_token.json()['content'])
        for token in tokens:
            kwargs = {'token': token, 'name': user_to_lock}
            requests.post((generate_full_url(Endpoints.locked_user) + user_to_lock), params=kwargs)
            locked_users_request1 = self.get_locked_users(kwargs)
            self.assertNotIn(user_to_lock, locked_users_request1.text)

    def test_locking_unexisting_user(self):
        """Test  functionality of locking unexisting users"""
        fake_users = InitFake.fake_users.copy()
        passwords = ['', 'password', 'birthday', 'petname']
        for user in fake_users.keys():
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.admin_token}
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertAlmostEqual(locked_users, '')

    def test_get_locked_amins_user_token(self):
        """Discovering locked admins with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        tokens = []
        passwords = ['', 'password', 'birthday', 'petname']
        for password in passwords:
            self.login('admin', password)
        for user, password in users.items():
            login_for_token = self.login(user, password)
            tokens.append(login_for_token.json()['content'])
        for token in tokens:
            kwargs = {'token': token}
            locked_admins_request = self.get_locked_admins(kwargs)
            locked_admin = locked_admins_request.json()['content']
            self.assertEqual(locked_admin, '')

    def test_get_locked_admins_empty_token(self):
        """Discovering locked admins with empty token"""
        passwords = ['', 'password', 'birthday', 'petname']
        for password in passwords:
            self.login('admin', password)
        kwargs = {'token': ''}
        locked_admins_request = self.get_locked_admins(kwargs)
        locked_admin = locked_admins_request.json()['content']
        self.assertEqual(locked_admin, '')

    def test_get_locked_users_user_token(self):
        """Discovering locked users with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        us, pas = users.popitem()
        login_for_user_token = self.login(us, pas)
        user_token = login_for_user_token.json()['content']
        passwords = ['', 'password', 'birthday', 'petname']
        for user in users.keys():
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': user_token}
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_get_locked_users_empty_token(self):
        """Discovering locked users with empty token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        passwords = ['', 'password', 'birthday', 'petname']
        for user in users.keys():
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': ''}
        locked_users_request = self.get_locked_users(kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')


