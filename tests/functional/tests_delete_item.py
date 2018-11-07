"""Functional tests for delete item"""

from random import randint, choice

from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN
from tests.functional import ApiTestBase


ITEM_NAME = choice(ITEM_NAMES)
ITEM_INDEX = randint(0, 1000)


class TestDeleteItem(ApiTestBase):
    """Class for tests of delete item"""

    def test_delete_item(self):
        """Test delete item when user has item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
                delete_item_response = self.application.delete_item(ITEM_INDEX, token)
                self.assertEqual(VALID_STATUS_CODE, delete_item_response.status_code)
                self.assertTrue(delete_item_response.json()["content"])

    def test_delete_empty_item(self):
        """Test can not delete item when user has not any items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                delete_item_response = self.application.delete_item(ITEM_INDEX, token)
                self.assertEqual(VALID_STATUS_CODE, delete_item_response.status_code)
                self.assertFalse(delete_item_response.json()["content"])

    def test_delete_item_invalid_token(self):
        """Test can not delete item with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
                delete_item_response = self.application.delete_item(ITEM_INDEX, INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, delete_item_response.status_code)
                self.assertFalse(delete_item_response.json()["content"])
