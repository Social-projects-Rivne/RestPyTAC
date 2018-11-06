"""Functional tests for all items"""

from tests.constants.constants import InitUsers, INVALID_TOKEN, VALID_STATUS_CODE
from tests.functional import ApiTestBase


class TestAllItems(ApiTestBase):
    """Class for tests of all items"""

    def test_without_items(self):
        """Test get all items when user has not any items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                get_all_items_response = self.application.get_all_items(token)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertFalse(get_all_items_response.json()["content"])

    def test_with_items(self):
        """Test get all items when user has items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(1, token, "Product")
                self.application.add_item(2, token, "Car")
                get_all_items_response = self.application.get_all_items(token)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertNotEqual("", get_all_items_response.json()["content"])
                self.assertTrue(get_all_items_response.json()["content"])

    def test_items_by_invalid_token(self):
        """Test can not get all items with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(1, token, "Product")
                self.application.add_item(2, token, "Car")
                get_all_items_response = self.application.get_all_items(INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertFalse(get_all_items_response.json()["content"])
