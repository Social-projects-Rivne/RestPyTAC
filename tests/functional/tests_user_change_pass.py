"""Testing ability to change password with existing users
For getting valid response we need token of that user, old password and new password"""

from tests.constants.constants import UserToTest, InvalidValues
from tests.functional import ApiTestBase
from ddt import ddt, idata


@ddt
class TestChangePass(ApiTestBase):
    """Testing server for ability to change pass with valid data and not valid data"""

    def setUp(self):
        """Get user token"""

        super().setUp()
        response = self.application.login(UserToTest.login, UserToTest.password)
        self.token = response.json()['content']
        self.assertEqual(200, response.status_code, "login error")

    def test_change_pass_valid_data(self):
        """Change pass with valid data"""

        # change pass
        new_pass = UserToTest.password + "wk"
        change_pass = self.application.change_pass(self.token, UserToTest.password, new_pass)
        self.assertEqual(200, change_pass.status_code)
        self.assertIn("true", change_pass.text)


        # login with changed pass
        login_with_new_pass = self.application.login(UserToTest.login, new_pass)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertEqual(32, len_token)

    @idata(InvalidValues.values)
    def test_change_pass(self, value):
        """Change pass with invalid values(negative)"""

        # change pass
        change_pass = self.application.change_pass(self.token, UserToTest.password, value)
        self.assertEqual(200, change_pass.status_code)
        self.assertNotIn('true', change_pass.text)

        # login with changed pass
        login_with_new_pass = self.application.login(UserToTest.login, value)
        len_token = len(login_with_new_pass.json()['content'])
        self.assertEqual(200, login_with_new_pass.status_code)
        self.assertIn("ERROR, user not found", len_token, "Pass changed to wrong: " + value)
