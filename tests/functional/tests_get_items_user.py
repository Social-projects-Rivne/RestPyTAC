from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser


class Test(ApiTestBase):
        """get user items with admintoken"""
        def test_items_admintoken(self):
            admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
            for k in dict.keys(InitUsers.users):
                get_items_user_response = self.get_user_items(k, admintoken)
                self.assertEqual(200, get_items_user_response.status_code)
                self.assertEqual("", get_items_user_response.json()["content"])

        """get user items with user token"""
        def test_items_usertoken(self):
            for k, v in dict.items(InitUsers.users):
                token = self.login(k, v).json()["content"]
                get_items_user_response = self.get_user_items(k, token)
                self.assertEqual(200, get_items_user_response.status_code)
                self.assertEqual("", get_items_user_response.json()["content"])
