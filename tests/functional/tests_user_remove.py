from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser



class TestRemoveUser(ApiTestBase):

    def setUp(self):

        """Get admin token"""

        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']
    #
    # def tearDown(self):
    #     """Reset api after each test"""
    #     super().tearDown()

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
        len_token = len(get_answer)
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer)
        self.assertNotEqual(32, len_token)

    def test_user_not_exist_deletion(self):

        """Detele not exist user"""

        removed_user = self.delete_user(self.adminToken, "testuser")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)

        self.assertNotIn('True', get_answer, "ERROR, we deleted not existed user")


    def test_user_not_valid(self):
        """Delete user with not valid name"""

        removed_user = self.delete_user(self.adminToken, "akimatg")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer, "ERROR, we deleted user with wrong nickname")

