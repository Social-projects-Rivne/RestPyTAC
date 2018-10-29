from tests.functional import ApiTestBase


class TestChangePass(ApiTestBase):

    def test_User_change_pass_valid_data(self):
        """login with exist user and change pass"""

        login = self.login("vbudktc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # change pass
        change_pass = self.change_pass(userToken, "qwerty", "qwerty")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "change pass error")

        # login with changed pass
        login_with_new_pass = self.login("vbudktc", "qwerty")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertEqual(32, len_token, "login with changed pass error")
        self.tearDown()

    def test_add_space_to_the_new_pass(self):
        """add 1 space to the new pass"""

        login = self.login("vbudktc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # change pass
        change_pass = self.change_pass(userToken, "qwerty", "qwerty ")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "change pass error")

        # login with changed pass
        login_with_new_pass = self.login("vbudktc", "qwerty ")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass contain space!")
        self.tearDown()

    def test_pass_contain_spaces_only(self):
        """use spaces only for new pass"""

        login = self.login("vbudktc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # change pass
        change_pass = self.change_pass(userToken, "qwerty", "     ")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "change pass error")

        # login with changed pass
        login_with_new_pass = self.login("vbudktc", "     ")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Password created from spaces")
        self.tearDown()

    def test_leave_pass_without_data(self):
        """don't enter any data to the new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field is empty")
        self.tearDown()

    def test_enter_symbols(self):
        """enter "!@#$%^&*()><" to the new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "!@#$%^&*()><")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "!@#$%^&*()><")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field contain !@#$%^&*()")
        self.tearDown()

    def test_use_cyrillic_letters(self):
        """use cyrillic letters in new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "ыва")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "ыва")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field contain cyrillic letters "
                                           "= ыва")
        self.tearDown()

    def test_use_ASCII_symbols(self):
        """use_ASCII_symbols in new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "Æð")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "Æð")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field contain ASCII symbols "
                                           "Æð")
        self.tearDown()

    def test_use_Japan_language(self):

        """use japan world in new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "本")
        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "本")
        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field contain japan world "
                                           "本")
        self.tearDown()

    def test_use_very_long_pass(self):
        """use very long new pass"""

        login = self.login("vvasylystc", "qwerty")
        userToken = login.json()['content']
        self.assertEqual(200, login.status_code, "login error")

        # leave pass without any data
        change_pass = self.change_pass(userToken, "qwerty", "5555555555555555555555555555555555555555555555555555555555"
                                                            "5555555555555555555555555555555555555555555555555555555555"
                                                            "5555555555555555555555555555555555555555555555555555555555"
                                                            "5555555555555555555555555555555555555555555555555555555555"
                                       )

        self.assertIn("true", change_pass.text)
        self.assertEqual(200, change_pass.status_code, "pass")

        # login with changed pass
        login_with_new_pass = self.login("vvasylystc", "5555555555555555555555555555555555555555555555555555555555"
                                                       "5555555555555555555555555555555555555555555555555555555555"
                                                       "5555555555555555555555555555555555555555555555555555555555"
                                                       "5555555555555555555555555555555555555555555555555555555555"
                                         )

        len_token = len(login.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code, "login with changed pass error")
        self.assertNotEqual(32, len_token, "Logged in with changed pass. Error!!! Pass field is too long, contain 410 "
                                           "digits")

        self.tearDown()
