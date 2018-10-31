"""Testing ability to change password with existing users
For getting valid response we need token of that user, old password and new password"""

from tests.constants.constants import UserToTest, InvalidValues
from tests.functional import ApiTestBase


class TestChangePass(ApiTestBase):
    """Testing server for ability to change pass with valid data and not valid data"""

    def setUp(self):
        """Get user token"""

        super().setUp()
        response = self.login(UserToTest.login, UserToTest.password)
        self.token = response.json()['content']
        self.assertEqual(200, response.status_code, "login error")

    def test_change_pass_valid_data(self):
        """Change pass with valid data"""

        # change pass
        valid_pass = UserToTest.password
        change_pass = self.change_pass(self.token, UserToTest.password, valid_pass)
        self.assertEqual(200, change_pass.status_code)
        self.assertTrue(change_pass.text)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, valid_pass)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertEqual(32, len_token)

    def test_add_space_to_the_new_pass(self):
        """add 1 space to the new pass"""

        pass_with_space = InvalidValues.values[0]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_with_space)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_with_space)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "New pass contain spaces")

    def test_pass_contain_spaces(self):
        """Use spaces only for new pass"""

        pass_only_spaces = InvalidValues.values[1]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_only_spaces)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_only_spaces)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "changed pass contain spaces only")

    def test_leave_pass_without_data(self):
        """don't enter any data to the new pass"""

        no_pass = InvalidValues.values[2]
        change_pass = self.change_pass(self.token, UserToTest.password, no_pass)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, no_pass)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "Pass field was empty")

    def test_enter_symbols(self):
        """enter "!@#$%^&*()><" to the new pass"""

        pass_contain_symbols = InvalidValues.values[3]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_contain_symbols)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_contain_symbols)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "Pass contain !@#$%^&*()><")
        self.assertFalse(login_with_new_pass.text)

    def test_use_cyrillic_letters(self):
        """use cyrillic letters in new pass"""

        pass_cyrillic = InvalidValues.values[4]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_cyrillic)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_cyrillic)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "Pass contain cyrillic letters")
        self.assertFalse(login_with_new_pass.text)

    def test_use_ascii_symbols(self):
        """use_ASCII_symbols in new pass"""

        pass_ascii_symbols = InvalidValues.values[5]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_ascii_symbols)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_ascii_symbols)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "Pass contain ASCII symbols")
        self.assertFalse(login_with_new_pass.text)

    def test_use_japan_language(self):
        """use japan world in new pass"""

        pass_japan = InvalidValues.values[6]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_japan)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_japan)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "pass contain Japan language")
        self.assertFalse(login_with_new_pass.text)

    def test_too_long_pass(self):
        """use very long new pass"""

        pass_too_long = InvalidValues.values[7]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_too_long)
        self.assertEqual(200, change_pass.status_code)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_too_long)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "pass is too long")
        self.assertFalse(login_with_new_pass.text)

    def too_short_pass(self):
        """user very short pass(only 1 letter)"""

        pass_too_short = InvalidValues.values[8]
        change_pass = self.change_pass(self.token, UserToTest.password, pass_too_short)
        self.assertEqual(200, change_pass.status_code)
        self.assertFalse(change_pass.text,)

        # login with changed pass
        login_with_new_pass = self.login(UserToTest.login, pass_too_short)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertNotEqual(32, len_token, "pass is too short")
        self.assertFalse(login_with_new_pass.text)
