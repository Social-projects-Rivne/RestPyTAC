"""Functional tests for get item indexes"""

from random import choice, randint

from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN
from tests.functional import ApiTestBase


ITEM_NAME = choice(ITEM_NAMES)
ITEM_INDEX = randint(0, 1000)


class TestGetItemIndexes(ApiTestBase):
    """Class for tests of get item indexes"""

    def test_get_empty_item_indexes(self):
        """Test get item indexes when user has not item indexes"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                get_item_indexes_response = self.application.get_item_indexes(token)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertFalse(get_item_indexes_response.json()["content"])

    def test_get_item_indexes(self):
        """Test get item indexes when user has any item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
                get_item_indexes_response = self.application.get_item_indexes(token)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertTrue(get_item_indexes_response.json()["content"])

    def test_get_item_indexes_by_invalid_token(self):
        """Test get item indexes with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.application.login(user, password).json()["content"]
                self.application.add_item(ITEM_INDEX, token, ITEM_NAME)
                get_item_indexes_response = self.application.get_item_indexes(INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertFalse(get_item_indexes_response.json()["content"])
