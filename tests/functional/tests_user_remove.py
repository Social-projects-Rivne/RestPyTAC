"""Testing ability to remove user
For getting valid response we need admin token and user name"""

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class TestRemoveUser(ApiTestBase):

    """Remove user with valid and not valid data"""

    def setUp(self):

        """Get admin token"""

        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.admin_token = response.json()['content']

    def test_remove_user(self):

        """delete user with valid data"""

        removed_user = self.delete_user(self.admin_token, "akimatc")
        get_answer = str(removed_user.json()['content'])
        self.assertIn('True', get_answer)
        self.assertEqual(200, removed_user.status_code)

        # search user in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertNotIn("akimatc", get_user_list.text)

    def test_delete_without_name(self):

        """Try to delete user without name, only with token"""

        removed_user = self.delete_user(self.admin_token, "")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer, "Error, we got deletion = True, without name")

    def test_delete_without_token(self):

        """Try to delete user without token, only with name"""

        removed_user = self.delete_user("", "akimatc")
        get_answer = str(removed_user.json()['content'])
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer, "Error, we got deletion without token")


    def test_admin_delete_himself(self):

        """Delete admin"""

        removed_user = self.delete_user(self.admin_token, DefaultUser.user)
        get_answer = str(removed_user.json()['content'])
        self.assertIn('True', get_answer)
        self.assertEqual(200, removed_user.status_code)

        # search user in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertIn("admin", get_user_list.text, "Error, admin has deleted himself")

        # Try to login with deleted admin
        login = self.login(DefaultUser.user, DefaultUser.password)
        response = login.json()['content']
        let_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotIn('True', login.content.text)
        self.assertNotEqual(32, let_token)
        self.assertNotEqual('ERROR, user not found', response, "Error, admin has deleted himself")

    def test_user_delete_himself(self):

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

        # search user in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertIn("akimatc", get_user_list.text, "Error, user delete himself with user token")

    def test_user_token_delete_admin(self):

        """Login with user and use user token to delete admin"""

        # login with user and get user token
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

        # search admin in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertIn("admin", get_user_list.text, "Error, user delete admin with user token")

    def test_admin_token_not_right(self):

        """Use wrong token"""

        invalid_token = "0123456789ABCDEF0123456789ABCDEF"
        removed_user = self.delete_user(invalid_token, "akimatc")
        get_answer = str(removed_user.json()['content'])
        len_token = len(get_answer)
        self.assertEqual(200, removed_user.status_code)
        self.assertNotIn('True', get_answer)
        self.assertNotEqual(32, len_token)

        # search admin in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertIn("akimatc", get_user_list.text, "Error, user was deleted with wrong token")

    def test_user_not_exist_deletion(self):

        """Detele not exist user"""

        removed_user = self.delete_user(self.admin_token, "testuser")
        self.assertEqual(200, removed_user.status_code)

        # search testuser in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertNotIn("testuser", get_user_list.text, "Error, not exist user was deleted")

    def test_user_not_valid(self):

        """Delete user with not valid name"""

        removed_user = self.delete_user(self.admin_token, "akimatg")
        self.assertEqual(200, removed_user.status_code)

        # search akimatg in user list
        get_user_list = self.get_all_users(self.admin_token)
        self.assertNotIn("akimatg", get_user_list.text, "Error, not exist user was deleted")
