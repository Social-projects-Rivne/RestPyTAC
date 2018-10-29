from tests.functional import ApiTestBase
from random import randint
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE, INVALID_TOKEN


item_index = randint(0, 1000)


class TestUserItemByIndex(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_user_item_by_admin(self):
        """get user item with admin token"""
        for user in dict.keys(InitUsers.users):
            admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
            get_item_user_response = self.get_user_item_by_index(item_index, user, admintoken)
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])

    def test_get_user_item_by_user(self):
        """get user item with user token"""
        counter = 0
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            get_item_user_response = self.get_user_item_by_index(counter, user, token)
            counter = counter + 1
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])

    def test_get_user_item_by_invalid_token(self):
        """get user item with invalid token"""
        for user in dict.keys(InitUsers.users):
            self.login(DefaultUser.user, DefaultUser.password)
            get_item_user_response = self.get_user_item_by_index(item_index, user, INVALID_TOKEN)
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])
