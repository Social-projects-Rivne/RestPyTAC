"""Testing ability to create new user
For getting valid response we need admin token, new user name, new password and give him admin rights"""

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser, NewUser, UserToTest, InvalidValues


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
        self.assertEqual(200, create_new_user.status_code)
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

    def test_add_spaces_to_login(self):
        """create new user with spaces on login"""

        login_with_space = InvalidValues.values[0]
        create_new_user = self.create_new_user(self.admin_token, login_with_space, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_with_space, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "User was created with spaces in login!")

    def test_login_contain_only_spaces(self):
        """create new user with only spaces on login"""

        login_spaces_only = InvalidValues.values[1]
        create_new_user = self.create_new_user(self.admin_token, login_spaces_only, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_spaces_only, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with spaces only in login!")

    def test_login_is_empty(self):
        """create new user with empty login """

        login_empty = InvalidValues.values[2]
        create_new_user = self.create_new_user(self.admin_token, login_empty, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login("", NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with empty login!")

    def test_login_contain_symbols(self):
        """Login contain !@#$%^&*()<> """

        login_symbols = InvalidValues.values[3]
        create_new_user = self.create_new_user(self.admin_token, login_symbols, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_symbols, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with !@#$%^&*()<> in login!")

    def test_login_contain_cyrillic_letters(self):
        """Login contain cyrillic letters"""

        login_cyrillic = InvalidValues.values[4]
        create_new_user = self.create_new_user(self.admin_token, login_cyrillic, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_cyrillic, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with cyrillic letters in login")

    def test_login_contain_ascii_symbols(self):
        """Login contain ASCII symbols"""

        login_ascii = InvalidValues.values[5]
        create_new_user = self.create_new_user(self.admin_token, login_ascii, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_ascii, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. New user was created with ASCII symbols in login")

    def test_login_contain_japan_symbols(self):

        """Login contain Japan symbols"""

        login_japan = InvalidValues.values[6]
        create_new_user = self.create_new_user(self.admin_token, login_japan, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_japan, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with Japan symbols in login")

    def test_login_is_too_long(self):

        """Login is too long"""

        login_too_long = InvalidValues.values[7]
        create_new_user = self.create_new_user(self.admin_token, login_too_long, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_too_long, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, " User was created with too long login")

    def test_login_is_too_short(self):
        """Login is too short"""

        login_too_short = InvalidValues.values[8]
        create_new_user = self.create_new_user(self.admin_token, login_too_short, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(login_too_short, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, " User was created with too short login")

    def test_pass_contain_spaces(self):
        """Pass contain spaces"""

        pass_with_spaces = InvalidValues.values[0]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_with_spaces, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_with_spaces)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with spaces in password")

    def test_pass_contain_only_spaces(self):
        """Pass contain spaces only"""

        pass_spaces_only = InvalidValues.values[1]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_spaces_only, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_spaces_only)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with spaces only in password!")

    def test_pass_is_empty(self):
        """create new user with empty pass"""

        pass_empty = InvalidValues.values[2]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_empty, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_empty)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with empty pass!")

    def test_pass_contain_symbols(self):
        """Pass contain !@#$%^&*()<> """

        pass_symbols = InvalidValues.values[3]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_symbols, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_symbols)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with !@#$%^&*()<> in password")

    def test_pass_contain_cyrillic_letters(self):
        """Pass contain cyrillic letters"""

        pass_cyrillic = InvalidValues.values[4]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_cyrillic, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_cyrillic)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with cyrillic letters in password")

    def test_pass_contain_ascii_symbols(self):
        """Login contain ASCII symbols"""

        pass_ascii = InvalidValues.values[5]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_ascii, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_ascii)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with ASCII symbols in password")

    def test_pass_contain_Japan_symbols(self):
        """pass contain Japan symbols"""

        pass_japan = InvalidValues.values[6]
        create_new_user = self.create_new_user(self.admin_token, NewUser.name, pass_japan, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(NewUser.name, pass_japan)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with Japan symbols in pass")

    def test_pass_is_too_long(self):
        """Password is too long"""

        pass_too_long = InvalidValues.values[7]
        create_new_user = self.create_new_user(self.admin_token, pass_too_long, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(pass_too_long, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with too long password")

    def test_pass_is_too_short(self):
        """Password is too short"""

        pass_too_short = InvalidValues.values[8]
        create_new_user = self.create_new_user(self.admin_token, pass_too_short, NewUser.password, NewUser.isUser)
        self.assertTrue(create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)

        # try to login with new user
        login = self.login(pass_too_short, NewUser.password)
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "User was created with too long password")
