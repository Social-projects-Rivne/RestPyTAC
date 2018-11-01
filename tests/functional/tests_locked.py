"""Testing functionality of locking users"""

import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser, InitUsers, InitFake, NewUser
from tests.utils.helper import generate_full_url
from random import choice


class TestLocked(ApiTestBase):
    """Testing functionality of locking users"""

    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        self.admin_token = response.json()['content']
        self.kwargs = {'token': self.admin_token}

    def tearDown(self):
        """Reset api after each test"""
        requests.get(generate_full_url(Endpoints.reset))

    def test_locked(self):
        """Test  functionality of locking users"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user = choice(list(users.keys()))  # returning random user
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
        new_user_name = NewUser.name
        new_user_pass = NewUser.password
        self.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        wrong_password = InitFake.wrong_password
        for _ in range(3):
            self.login(new_user_name, wrong_password)
        locked_admins = self.get_locked_admins(self.kwargs)
        self.assertIn(new_user_name, locked_admins.text)

    def test_not_locked_admin(self):
        """Admin should not be locked"""
        new_user_name = NewUser.name
        new_user_pass = NewUser.password
        self.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        passwords = ['', 'password', new_user_pass]
        for password in passwords:
            self.login(new_user_name, password)
        locked_admins = self.get_locked_admins(self.kwargs)
        logined_admins = self.get_logined_admins(self.kwargs)
        self.assertNotIn(new_user_name, locked_admins.text)
        self.assertIn(new_user_name, logined_admins.text)

    def test_manual_lock_user_token(self):
        """Test  functionality of locking users by manual command with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user, password = users.popitem()  # user for login
        user_to_lock = choice(list(users.keys()))  # returning random user for lock
        login_for_token = self.login(user, password)
        token = login_for_token.json()['content']
        fake_kwargs = {'token': token, 'name': user_to_lock}
        self.lock_user(user_to_lock, fake_kwargs)
        locked_users_request1 = self.get_locked_users(self.kwargs)
        self.assertNotIn(user_to_lock, locked_users_request1.text)

    def test_locking_unexisting_user(self):
        """Test  functionality of locking unexisting users"""
        fake_user, fake_password = choice(list(InitFake.fake_users.items()))
        for _ in range(3):
            self.login(fake_user, fake_password)
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        print(repr(locked_users))
        self.assertEqual(locked_users, '')

    def test_get_locked_admins_user_token(self):
        """Discovering locked admins with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user, password = choice(list(users.items()))
        for _ in range(3):
            self.login(DefaultUser.user_admin, InitFake.wrong_password)  # locking admin
        login_for_token = self.login(user, password)
        token = login_for_token.json()['content']
        self.kwargs['token'] = token
        locked_admins_request = self.get_locked_admins(self.kwargs)
        locked_admin = locked_admins_request.json()['content']
        self.assertEqual(locked_admin, '')

    def test_get_locked_admins_empty_token(self):
        """Discovering locked admins with empty token"""
        for _ in range(3):
            self.login(DefaultUser.user_admin, InitFake.wrong_password)
        self.kwargs['token'] = ''
        locked_admins_request = self.get_locked_admins(self.kwargs)
        locked_admin = locked_admins_request.json()['content']
        self.assertEqual(locked_admin, '')

    def test_get_locked_users_user_token(self):
        """Discovering locked users with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user, pasword = users.popitem()
        login_for_user_token = self.login(user, pasword)
        user_token = login_for_user_token.json()['content']
        user_to_lock = list(users.keys())[0]
        self.login(user_to_lock, InitFake.wrong_password)
        self.kwargs['token'] = user_token
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_get_locked_users_empty_token(self):
        """Discovering locked users with empty token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user_to_lock = list(users.keys())[0]
        for _ in range(3):
            self.login(user_to_lock, InitFake.wrong_password)
        self.kwargs['token'] = ''
        locked_users_request = self.get_locked_users(self.kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')