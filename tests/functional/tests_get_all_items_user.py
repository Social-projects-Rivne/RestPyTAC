"""Functional tests for get all items"""

from random import choice, randint
from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN


ITEM_INDEX = randint(0, 1000)
ITEM_NAME = choice(ITEM_NAMES)


class TestAllUserItems(ApiTestBase):
    """Class for tests of get all items"""

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_items_by_admin(self):
        """Test get user items with admintoken"""
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admintoken)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_items_by_admin_with_invalid_token(self):
        """Test get items by admin with invalid token"""
        self.login(DefaultUser.user, DefaultUser.password)
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_added_items_by_admin(self):
        """Test get added user items by admin"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(ITEM_INDEX, token, ITEM_NAME)
        admin_token = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admin_token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertTrue(get_items_user_response.json()["content"])

    def test_get_items_invalid_user(self):
        """Test get item invalid user"""
        admin_token = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        get_items_user_response = self.get_user_all_items(ITEM_NAME, admin_token)
        self.assertNotEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
        self.assertIn("Error", get_items_user_response.text)

    def test_get_items_by_user(self):
        """Test get user items with user token"""
        for user in InitUsers.users:
            with self.subTest(i=user):
                token = self.login("kilinatc", "qwerty").json()["content"]
                get_items_user_response = self.get_user_all_items(user, token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_added_items_by_user(self):
        """Test get added user items by user token"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(ITEM_INDEX, token, ITEM_NAME)
        token = self.login("akinatc", "qwerty").json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])
