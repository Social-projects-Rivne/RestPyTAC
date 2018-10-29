from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES


item_index = randint(0, 1000)
item_name = choice(ITEM_NAMES)


class TestUpdateItem(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_update_empty_item(self):
        """test update item when user has no item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                update_item_response = self.update_item(item_index, token, item_name)
                self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
                self.assertFalse(update_item_response.json()["content"])

    def test_update_item(self):
        """test update item when user has item"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(item_index, token, item_name)
            update_item_response = self.update_item(item_index, token, item_name)
            self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
            self.assertTrue(update_item_response.json()["content"])

    def test_update_item_invalid_index(self):
        """test update item when index not int"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                update_item_response = self.update_item(item_name, token, item_name)
                self.assertNotEqual(VALID_STATUS_CODE, update_item_response.status_code)
