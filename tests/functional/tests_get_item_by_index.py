"""Functional tests for get item by index"""

from random import choice, randint
from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN


ITEM_INDEX = randint(0, 1000)
ITEM_NAME = choice(ITEM_NAMES)


class TestGetItemByIndex(ApiTestBase):
    """Class for tests of get item by index"""

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_empty_item(self):
        """Test get item by index when user has not items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                get_item_response = self.get_item(ITEM_INDEX, token)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertFalse(get_item_response.json()["content"])

    def test_get_item(self):
        """Test get item by index when user has item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(ITEM_INDEX, token, ITEM_NAME)
                get_item_response = self.get_item(ITEM_INDEX, token)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertTrue(get_item_response.json()["content"])
                self.assertEqual(ITEM_NAME, get_item_response.json()["content"])

    def test_get_item_index_str(self):
        """Test get item by index with str index"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(ITEM_INDEX, token, ITEM_NAME)
                get_item_response = self.get_item("call", token)
                self.assertNotEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertIn("Bad Request", get_item_response.text)

    def test_get_item_index_invalid_token(self):
        """Test get item by index with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                self.login(user, password)
                get_item_response = self.get_item(ITEM_INDEX, INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertFalse(get_item_response.json()["content"])
