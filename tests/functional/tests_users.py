from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class TestUsers(ApiTestBase):
    """
    Testing response of "/users"
    """

    def test_get_all_users_admin(self):
        """
        Get the list of all users by admin
        """

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        req = self.get_all_users(token)

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])

    def test_get_all_users_user(self):
        """
        Get the list of all users by user (without admin rights)
        """

        login = self.login(DefaultUser.user_akimatc, DefaultUser.password_akimatc)
        token = login.json()["content"]

        req = self.get_all_users(token)

        self.assertEqual(req.status_code, 200)
        self.assertFalse(req.json()["content"])
