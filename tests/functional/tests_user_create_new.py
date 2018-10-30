from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class TestCreateNewUser(ApiTestBase):

    def setUp(self):

        """login admin and get admin token"""

        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_create_new_user(self):

        """create new user with valid data"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(32, len_of_new_user_token)
        self.tearDown()

    def test_create_new_with_exist_name(self):

        """create new user with already exist name"""

        create_new_user = self.create_new_user(self.adminToken, "admin", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("admin", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertEqual(200, login.status_code)
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with a name what already exist")
        self.tearDown()

    def test_create_user_with_non_admin_token(self):

        """create new user with usage of non admin token"""

        login = self.login("slototc", "qwerty")
        token = login.json()['content']
        create_new_user = self.create_new_user(token, "Username", "Pass", "false")
        self.assertIn("false", create_new_user.text, "ERROR, user was created with user token")
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "Pass")
        text_of_login_message = str(login.content)
        self.assertIn("ERROR", text_of_login_message, "ERROR, user was created with user token")
        self.tearDown()

    def test_give_invalid_admin_rights(self):

        """create new user with invalid admin rights"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "Pass", "admin")
        self.assertIn("Bad Request", create_new_user.text, "ERROR, user was created with invalid admin rights")
        self.assertEquals(400, create_new_user.status_code)
        self.assertNotEqual(200, create_new_user.status_code)
        login = self.login("Username", "Pass")
        text_of_login_message = str(login.content)
        self.assertIn("ERROR", text_of_login_message, "ERROR, user was created with invalid admin rights")
        self.tearDown()

    def test_create_user_add_spaces_to_login(self):

        """create new user with spaces on login"""

        create_new_user = self.create_new_user(self.adminToken, "Username  ", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username  ", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR, user was created with spaces in login!")
        self.tearDown()

    def test_login_contain_only_spaces(self):

        """create new user with only spaces on login"""

        create_new_user = self.create_new_user(self.adminToken, "     ", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("     ", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR, user was created with spaces only in login!")
        self.tearDown()

    def test_login_is_empty(self):

        """create new user with empty login """

        create_new_user = self.create_new_user(self.adminToken, "", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with empty login!")
        self.tearDown()

    def test_login_contain_symbols(self):

        """Login contain !@#$%^&*()<> """

        create_new_user = self.create_new_user(self.adminToken, "!@#$%^&*()<>", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("!@#$%^&*()<>", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with !@#$%^&*()<> in login!")
        self.tearDown()

    def test_login_contain_cyrillic_letters(self):

        """Login contain cyrillic letters"""

        create_new_user = self.create_new_user(self.adminToken, "ыва", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("ыва", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with cyrillic letters in login")
        self.tearDown()

    def test_login_contain_ASCII_symbols(self):

        """Login contain ASCII symbols"""

        create_new_user = self.create_new_user(self.adminToken, "ø¶", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("ø¶", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. New user was created with ASCII symbols in login")
        self.tearDown()

    def test_login_contain_Japan_symbols(self):

        """Login contain Japan symbols"""

        create_new_user = self.create_new_user(self.adminToken, "本本本本本", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("本本本本本", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with Japan symbols in login")
        self.tearDown()

    def test_login_is_too_long(self):

        """Login is too long"""

        create_new_user = self.create_new_user(self.adminToken, "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                "aaaaaaaaaaaaaaaaaaaaa", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with too long login")
        self.tearDown()

    def test_pass_contain_spaces(self):

        """Pass contain spaces"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "Pass  ", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "Pass  ")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with spaces in password")
        self.tearDown()

    def test_pass_contain_only_spaces(self):

        """Pass contain spaces only"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "     ", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "     ")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with spaces only in password!")
        self.tearDown()

    def test_pass_is_empty(self):

        """create new user with empty pass"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with empty pass!")
        self.tearDown()

    def test_pass_contain_symbols(self):

        """Pass contain !@#$%^&*()<> """

        create_new_user = self.create_new_user(self.adminToken, "Username", "!@#$%^&*()<>", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "!@#$%^&*()<>")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with !@#$%^&*()<> in password")
        self.tearDown()

    def test_pass_contain_cyrillic_letters(self):

        """Pass contain cyrillic letters"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "ыва", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "ыва")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with cyrillic letters in password")
        self.tearDown()

    def test_pass_contain_ASCII_symbols(self):

        """Login contain ASCII symbols"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "ø¶", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "ø¶")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. New user was created with ASCII symbols in password")
        self.tearDown()

    def test_pass_contain_Japan_symbols(self):

        """pass contain Japan symbols"""

        create_new_user = self.create_new_user(self.adminToken, "Username", "本本本本本", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Username", "本本本本本")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with Japan symbols in pass")
        self.tearDown()

    def test_pass_is_too_long(self):

        """Password is too long"""

        create_new_user = self.create_new_user(self.adminToken, "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                "aaaaaaaaaaaaaaaaaaaaa", "Pass", "false")
        self.assertIn("true", create_new_user.text)
        self.assertEqual(200, create_new_user.status_code)
        login = self.login("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Pass")
        len_of_new_user_token = len(login.json()['content'])
        self.assertNotEqual(32, len_of_new_user_token, "ERROR. User was created with too long password")
        self.tearDown()