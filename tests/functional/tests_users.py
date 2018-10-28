from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class TestUsers(ApiTestBase):

    def test_get_all_users_admin(self):
        """
        Get the list of all users by admin
        :return:
        """

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.get_all_users(token)

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.ok)
        self.assertTrue(req.json()["content"])

    def test_get_all_users_user(self):
        """
        Get the list of all users by user (without admin rights)
        :return:
        """

        login = self.login(DefaultUser.user, DefaultUser.password)
        token = login.json()["content"]

        req = self.get_all_users(token)

        self.assertEqual(req.status_code, 200)
        self.assertFalse(req.json()["content"])
        self.assertTrue(req.ok)
