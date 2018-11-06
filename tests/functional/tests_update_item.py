"""Functional tests for update item"""

from random import choice, randint

from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN
from tests.functional import ApiTestBase


ITEM_INDEX = randint(0, 1000)
ITEM_NAME = choice(ITEM_NAMES)


class TestUpdateItem(ApiTestBase):
    """Class for tests of update item"""

    def test_update_item(self):
        """Test update item when user has item"""
        for user, password in InitUsers.users.items():
            token = self.application.login(user, password).json()["content"]
            self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
            update_item_response = self.application.update_item(ITEM_INDEX, token, ITEM_NAME)
            self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
            self.assertTrue(update_item_response.json()["content"])

    def test_update_empty_item(self):
        """Test can not update item when user has no item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                update_item_response = self.application.update_item(ITEM_INDEX, token, ITEM_NAME)
                self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
                self.assertFalse(update_item_response.json()["content"])

    def test_update_item_invalid_index(self):
        """Test can not update item when index not int"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
                update_item_response = self.application.update_item(ITEM_NAME, token, ITEM_NAME)
                self.assertNotEqual(VALID_STATUS_CODE, update_item_response.status_code)
                self.assertIn("Bad Request", update_item_response.text)

    def test_update_item_invalid_token(self):
        """Test can not update item with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                self.application.login(user, password)
                update_item_response = self.application.update_item(ITEM_INDEX, INVALID_TOKEN, ITEM_NAME)
                self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
                self.assertFalse(update_item_response.json()["content"])
