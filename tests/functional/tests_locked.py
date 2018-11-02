"""Testing functionality of locking users"""

from random import choice
from tests.constants.constants import DefaultUser, InitUsers, NewUser, Users
from tests.functional import ApiTestBase


class TestLocked(ApiTestBase):
    """Testing functionality of locking users"""

    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        self.admin_token = response.json()['content']
        self.kwargs = {'token': self.admin_token}

    def test_locked(self):
        """Test  functionality of locking user"""
        users = InitUsers.users.copy()
        user = choice(list(users.keys()))  # returning random user
        wrong_password = Users.fake_password
        for _ in range(3):
            self.application.login(user, wrong_password)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        locked_users = locked_users_request.json()['content']
        self.assertIn(user, locked_users)

    def test_not_locked(self):
        """User should not be locked"""
        users = InitUsers.users.copy()
        user = choice(list(users.keys()))  # returning random user
        wrong_passwords = ['', 'password']
        for wrong_password in wrong_passwords:
            self.application.login(user, wrong_password)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        locked_users = locked_users_request.json()['content']
        self.assertNotIn(user, locked_users)

    def test_manual_lock(self):
        """Test  functionality of locking users by manual command"""
        users = InitUsers.users.copy()
        user_to_lock = choice(list(users.keys()))  # returning random user
        self.application.lock_user(self.admin_token, user_to_lock)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        self.assertIn(user_to_lock, locked_users_request.text)

    def test_manual_unlock(self):
        """Test  functionality of unlocking users by manual command"""
        users = InitUsers.users.copy()
        user_to_lock = choice(list(users.keys()))  # returning random user
        wrong_password = Users.fake_password
        for _ in range(3):
            self.application.login(user_to_lock, wrong_password)
        self.application.unlock_user(self.admin_token, user_to_lock)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        locked_users = locked_users_request.text
        self.assertNotIn(user_to_lock, locked_users)

    def test_reset_locked_admin_token(self):
        """Test  functionality of unlocking all users with admin token"""
        users = InitUsers.users.copy()
        wrong_password = Users.fake_password
        for user in users.keys():
            self.application.login(user, wrong_password)
        self.application.unlock_all_users(self.admin_token)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_locked_admins(self):
        """Test functionality of locking admins"""
        new_user_name = NewUser.name
        new_user_pass = NewUser.password
        self.application.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        wrong_password = Users.fake_password
        for _ in range(3):
            self.application.login(new_user_name, wrong_password)
        locked_admins = self.application.get_locked_admins(self.admin_token)
        self.assertIn(new_user_name, locked_admins.text)

    def test_not_locked_admin(self):
        """Admin should not be locked"""
        new_user_name = NewUser.name
        new_user_pass = NewUser.password
        self.application.create_new_user(self.admin_token, new_user_name, new_user_pass, 'true')
        passwords = ['', 'password', new_user_pass]
        for password in passwords:
            self.application.login(new_user_name, password)
        locked_admins = self.application.get_locked_admins(self.admin_token)
        logined_admins = self.application.login_admins(self.admin_token)
        self.assertNotIn(new_user_name, locked_admins.text)
        self.assertIn(new_user_name, logined_admins.text)

    def test_manual_lock_user_token(self):
        """Test  functionality of locking users by manual command with user token"""
        users = InitUsers.users.copy()
        user, password = users.popitem()  # user for login
        user_to_lock = choice(list(users.keys()))  # returning random user for lock
        login_for_token = self.application.login(user, password)
        token = login_for_token.json()['content']
        self.application.lock_user(token, user_to_lock)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        self.assertNotIn(user_to_lock, locked_users_request.text)

    def test_locking_unexisting_user(self):
        """Test  functionality of locking unexisting users"""
        fake_user = Users.fake_user
        fake_password = Users.fake_password
        for _ in range(3):
            self.application.login(fake_user, fake_password)
        locked_users_request = self.application.get_locked_users(self.admin_token)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_get_locked_admins_user_token(self):
        """Discovering locked admins with user token"""
        users = InitUsers.users.copy()
        user, password = choice(list(users.items()))
        for _ in range(3):
            self.application.login(DefaultUser.user_admin, Users.fake_password)  # locking admin
        login_for_token = self.application.login(user, password)
        user_token = login_for_token.json()['content']
        locked_admins_request = self.application.get_locked_admins(user_token)
        locked_admin = locked_admins_request.json()['content']
        self.assertEqual(locked_admin, '')

    def test_get_locked_admins_empty_token(self):
        """Discovering locked admins with empty token"""
        for _ in range(3):
            self.application.login(DefaultUser.user_admin, Users.fake_password)
        token = ''
        locked_admins_request = self.application.get_locked_admins(token)
        locked_admin = locked_admins_request.json()['content']
        self.assertEqual(locked_admin, '')

    def test_get_locked_users_user_token(self):
        """Discovering locked users with user token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user, pasword = users.popitem()
        login_for_user_token = self.application.login(user, pasword)
        user_token = login_for_user_token.json()['content']
        user_to_lock = list(users.keys())[0]
        self.application.login(user_to_lock, Users.fake_password)
        locked_users_request = self.application.get_locked_users(user_token)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')

    def test_get_locked_users_empty_token(self):
        """Discovering locked users with empty token"""
        users = InitUsers.users.copy()
        users.pop('admin', None)
        user_to_lock = list(users.keys())[0]
        for _ in range(3):
            self.application.login(user_to_lock, Users.fake_password)
        token = ''
        locked_users_request = self.application.get_locked_users(token)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')
