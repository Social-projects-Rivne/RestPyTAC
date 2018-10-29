"""Functional tests for get user item by index"""

from random import randint
from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE, INVALID_TOKEN


ITEM_INDEX = randint(0, 1000)


class TestUserItemByIndex(ApiTestBase):
    """Class for tests of get user item by index"""

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_user_item_by_admin(self):
        """Test get user item by index with admin token"""
        for user in dict.keys(InitUsers.users):
            admin_token = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
            get_item_user_response = self.get_user_item_by_index(ITEM_INDEX, user, admin_token)
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])

    def test_get_user_item_by_user(self):
        """Test get user item by index with user token"""
        counter = 0
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            get_item_user_response = self.get_user_item_by_index(counter, user, token)
            counter = counter + 1
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])

    def test_get_user_item_by_invalid_token(self):
        """Test get user item by index with invalid token"""
        for user in dict.keys(InitUsers.users):
            self.login(DefaultUser.user, DefaultUser.password)
            get_item_user_response = self.get_user_item_by_index(ITEM_INDEX, user, INVALID_TOKEN)
            self.assertEqual(VALID_STATUS_CODE, get_item_user_response.status_code)
            self.assertFalse(get_item_user_response.json()["content"])
