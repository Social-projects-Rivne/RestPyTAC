import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestRemoveUser(ApiTestBase):

    def setUp(self):

        """Get admin token"""

        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

        def tearDown(self):

            """Reset api after each test"""
            requests.get(generate_full_url(Endpoints.reset))

    def test_remove_user(self):

        """delete user with valid data"""

        removed_user = self.delete_user(self.adminToken, "akimatc")
        get_answer = str(removed_user.json()['content'])
        self.assertIn('True', get_answer)
        self.assertEqual(200, removed_user.status_code)

        # Try to login with removed user

        login = self.login("akimatc", "qwerty")
        response = login.json()['content']
        let_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotIn('True', str(login.content))
        self.assertNotEqual(32, let_token)
        self.assertEqual('ERROR, user not found', response)


    def test_admin_delete_himself(self):

        """Delete admin"""

        removed_user = self.delete_user(self.adminToken, DefaultUser.user)
        get_answer = str(removed_user.json()['content'])
        self.assertIn('True', get_answer)
        self.assertEqual(200, removed_user.status_code)

        # Try to login with deleted admin

        login = self.login(DefaultUser.user, DefaultUser.password)
        response = login.json()['content']
        let_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotIn('True', str(login.content))
        self.assertNotEqual(32, let_token)
        self.assertEqual('ERROR, user not found', response)


    def test_user_detele_himself(self):

        """User delete himself with user token"""

        login = self.login("akimatc", "qwerty")
        token = login.json()['content']
        let_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertEqual(32, let_token)

        # Use User token to delete himself
        removed_user = self.delete_user(token, "akimatc")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertIn('False', get_answer, 'ERROR. User was deleted with user token!')
        self.assertNotEqual(32, len(get_answer))


    def test_user_token_delete_admin(self):

        """Login with user and use user token to delete admin"""

        login = self.login("akimatc", "qwerty")
        token = login.json()['content']
        let_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertEqual(32, let_token)

        # del admin with user token
        removed_user = self.delete_user(token, "admin")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertIn('False', get_answer, 'ERROR. Admin was deleted with user token!')
        self.assertNotEqual(32, len(get_answer))

    def test_admin_token_not_right(self):

        """Use wrong token"""

        invalid_token = "0123456789ABCDEF0123456789ABCDEF"
        removed_user = self.delete_user(invalid_token, "akimatc")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer)

    def test_user_not_exist_deletion(self):
        ...

    #
    # def test_user_not_valid(self):
    #     ...
    #
    # def test_token_not_valid(self):
    #     ...
    # def test_remove_User_with_valid_data(self):
    #
    #     #delete test user
    #     remove_created_user = requests.delete(generate_full_url(Endpoints.user),
    #                                         params={'token': self.adminToken, "name": "testuserdelete"})
    #     self.assertIn("true", remove_created_user.text)
    #
    #
    # def test_login_deleted_user(self):
    #     deleted_user_login = requests.post(generate_full_url(Endpoints.login),
    #                                         params = {"name": "testuserdelete", "password": "qwerty"})
    #     self.assertIn("ERROR", deleted_user_login.text, "Error, user not deleted")
    #

