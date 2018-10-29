"""Functional tests for add item"""

from random import choice, randint
from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, INVALID_TOKEN, VALID_STATUS_CODE, ITEM_NAMES


ITEM_INDEX = randint(0, 1000)
ITEM_NAME = choice(ITEM_NAMES)


class TestAddItem(ApiTestBase):
    """Class for tests add item"""

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_add_item_positive(self):
        """Test add item with valid token"""
        counter = 0
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(counter, token, ITEM_NAME)
                counter = counter + 1
                self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
                self.assertTrue(add_item_user_response.json()["content"])

    def test_add_specific_item(self):
        """Test add item with specific item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(ITEM_INDEX, token, ITEM_NAME)
                get_item_response = self.get_item(ITEM_INDEX, token)
                self.assertEqual(ITEM_NAME, get_item_response.json()["content"])

    def test_add_item_negative(self):
        """Test add item with invalid token"""
        add_item_user_response = self.add_item(ITEM_INDEX, INVALID_TOKEN, ITEM_NAME)
        self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
        self.assertFalse(add_item_user_response.json()["content"])

    def test_add_item_invalid_index(self):
        """Test add item when index not int"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(ITEM_NAME, token, ITEM_NAME)
                self.assertNotEqual(VALID_STATUS_CODE, add_item_user_response.status_code)

    def test_add_int_item(self):
        """Test add item with only number"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(ITEM_INDEX, token, ITEM_INDEX)
                self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
                self.assertFalse(add_item_user_response.json()["content"])
