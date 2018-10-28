from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser


class Test(ApiTestBase):
    """get user item with admin token"""
    def test_get_user_item_byadmin(self):
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        counter = 1
        for user in dict.keys(InitUsers.users):
            get_item_user_response = self.get_user_item(counter, user, admintoken)
            counter = counter + 1
            self.assertEqual(200, get_item_user_response.status_code)
            self.assertEqual("", get_item_user_response.json()["content"])

    """get user item with user token"""
    def test_get_user_item_byuser(self):
        counter = 0
        for k, v in dict.items(InitUsers.users):
            token = self.login(k, v).json()["content"]
            get_item_user_response = self.get_user_item(counter, k, token)
            counter = counter + 1
            self.assertEqual(200, get_item_user_response.status_code)
            self.assertEqual("", get_item_user_response.json()["content"])
