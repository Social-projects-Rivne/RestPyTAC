from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE


class Test(ApiTestBase):

    def test_get_user_item_by_admin(self):
        """get user item with admin token"""
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        counter = 0
        for user in dict.keys(InitUsers.users):
            get_item_user_response = self.get_user_item(counter, user, admintoken)
            counter = counter + 1
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertEqual("", get_item_user_response.json()["content"])

    def test_get_user_item_by_user(self):
        """get user item with user token"""
        counter = 0
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            get_item_user_response = self.get_user_item(counter, user, token)
            counter = counter + 1
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertEqual("", get_item_user_response.json()["content"])
