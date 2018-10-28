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
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        users = list(InitUsers.users)
        users.remove('admin')
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        locked_users_request = requests.get(generate_full_url(Endpoints.locked_users), params=kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users,
                         ('0 \totlumtc\n1 \tvbudktc\n2 \tvvasylystc\n3 \tkhalaktc\n4'
                          ' \tslototc\n5 \tOKonokhtc\n6 \takimatc\n7 \tkilinatc\n'))
        requests.get(generate_full_url(Endpoints.reset))  # reset api

    def test_not_locked(self):
        """User should not be locked"""
        passwords = ['', 'password', 'qwerty']
        users = list(InitUsers.users)
        users.remove('admin')
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        logined_users_request = requests.get(generate_full_url(Endpoints.login_users), params=kwargs)
        logined_users = logined_users_request.json()['content']
        # print(repr(logined_users))
        self.assertEqual(logined_users, ('0 \totlumtc\n1 \tvbudktc\n2 \tvvasylystc\n3 \tadmin\n4'
                                         ' \tslototc\n5 \tOKonokhtc\n6 \takimatc\n7 \tkilinatc\n'))

    def test_manual_lock(self):
        """Test  functionality of locking users by manual command"""
        users = list(InitUsers.users)
        users.remove('admin')
        kwargs = {'token': self.adminToken, 'name': users[1]}
        requests.post((generate_full_url(Endpoints.locked_user) + users[1]), params=kwargs)
        locked_users_request1 = requests.get(generate_full_url(Endpoints.locked_users),
                                             params={'token': self.adminToken})
        locked_users = locked_users_request1.json()['content']
        s = '0 \t' + users[1] + '\n'
        self.assertEqual(locked_users, s)

    def test_manual_unlock(self):
        """Test  functionality of unlocking users by manual command"""
        users = list(InitUsers.users)
        users.remove('admin')
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        for password in passwords:
            self.login(users[3], password)
        kwargs = {'token': self.adminToken, 'name': users[3]}
        requests.put((generate_full_url(Endpoints.locked_user) + users[3]), params=kwargs)
        locked_users_request = requests.get(generate_full_url(Endpoints.locked_users),
                                            params={'token': self.adminToken})
        locked_users = locked_users_request.text
        if users[3] in locked_users:
            self.assertTrue(False)

    def test_reset_locked(self):
        """Test  functionality of unlocking all users"""
        passwords = ['', 'password', 'birthday', 'petname']  # number of passwords determines login attemps
        users = list(InitUsers.users)
        users.remove('admin')
        for user in users:
            for password in passwords:
                self.login(user, password)
        kwargs = {'token': self.adminToken}
        requests.put(generate_full_url(Endpoints.locked_reset), params=kwargs)
        locked_users_request = requests.get(generate_full_url(Endpoints.locked_users), params=kwargs)
        locked_users = locked_users_request.json()['content']
        self.assertEqual(locked_users, '')
