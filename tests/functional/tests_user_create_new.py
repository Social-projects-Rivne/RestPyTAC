"""Testing ability to create new user
For getting valid response we need admin token, new user name, new password and give him admin rights"""

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser, NewUser, UserToTest, InvalidValues
from ddt import ddt, idata


@ddt
class TestCreateNewUser(ApiTestBase):
    """Create new user with valid and invalid data"""

    def setUp(self):
        """login admin and get admin token"""

        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.admin_token = response.json()['content']

    def test_create_new_user(self):

        """create new user with valid data"""

        create_new_user = self.create_new_user(self.admin_token, NewUser.name, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertEqual(32, len_of_new_user_token)

    def test_create_new_with_exist_name(self):
        """create new user with already exist name"""

        create_new_user = self.create_new_user(self.admin_token, DefaultUser.user, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(DefaultUser.user, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with a name what already exist")

    def test_with_non_admin_token(self):
        """create new user with usage of non admin token"""

        # login with existed user
        login = self.login(UserToTest.login, UserToTest.password)
        user_token = login.json()['content']

        # create new user with user token
        create_new_user = self.create_new_user(user_token, NewUser.name, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login_new_user = self.login(NewUser.name, NewUser.password)
        self.assertEqual(200, login_new_user.status_code)
        self.assertIn("ERROR", login_new_user.text, "User was created with user token")

    def test_give_invalid_admin_rights(self):
        """create new user with invalid admin rights"""

        create_new_user = self.create_new_user(self.admin_token, NewUser.name, NewUser.password, NewUser.wrong_rights)
        self.assertIn("Bad Request", create_new_user.text)
        self.assertEquals(400, create_new_user.status_code)
        self.assertNotEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, NewUser.password)
        text_of_login_message = str(login.content)
        self.assertIn("ERROR", text_of_login_message, "User was created with invalid admin rights")

    @idata(InvalidValues.values)
    def test_wrong_new_login(self, value):
        """create new user with spaces on login"""

        # login_with_space = InvalidValues.values[0]
        create_new_user = self.create_new_user(self.admin_token, value, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(value, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "Wrong login name: " + value)

    @idata(InvalidValues.values)
    def test_wrong_new_pass(self, value):
        """create new user with only spaces on login"""

        create_new_user = self.create_new_user(self.admin_token, NewUser.name, value, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, value)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with wrong pass: " + value)
