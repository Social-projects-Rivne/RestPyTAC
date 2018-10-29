from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE


class Test(ApiTestBase):

        def test_get_items_by_admin(self):
            """get user items with admintoken"""
            self.reset()
            admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
            for user in InitUsers.users:
                with self.subTest(i=user):
                    get_items_user_response = self.get_user_items(user, admintoken)
                    self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                    self.assertEqual("", get_items_user_response.json()["content"])

        def test_get_items_by_user(self):
            """get user items with user token"""
            for user, password in InitUsers.users.items():
                token = self.login(user, password).json()["content"]
                get_items_user_response = self.get_user_items(user, token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertEqual("", get_items_user_response.json()["content"])
