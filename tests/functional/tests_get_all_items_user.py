from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN


item_index = randint(0, 1000)
item_name = choice(ITEM_NAMES)


class TestAllUserItems(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_items_by_admin(self):
        """get user items with admintoken"""
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admintoken)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_items_by_admin_with_invalid_token(self):
        """get items by admin with invalid token"""
        self.login(DefaultUser.user, DefaultUser.password)
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_added_items_by_admin(self):
        """get added user items by admin"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(item_index, token, item_name)
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admintoken)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertTrue(get_items_user_response.json()["content"])

    def test_get_items_by_user(self):
        """get user items with user token"""
        for user in InitUsers.users:
            with self.subTest(i=user):
                token = self.login("kilinatc", "password").json()["content"]
                get_items_user_response = self.get_user_all_items(user, token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_added_items_by_user(self):
        """get added user items by user"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(item_index, token, item_name)
        admintoken = self.login("akinatc", "password").json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admintoken)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])
