from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, INVALID_TOKEN, VALID_STATUS_CODE, ITEM_NAMES


item_index = randint(0, 1000)
item_name = choice(ITEM_NAMES)


class TestAddItem(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_add_item_positive(self):
        """test with valid token"""
        counter = 0
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(counter, token, item_name)
                counter = counter + 1
                self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
                self.assertTrue(add_item_user_response.json()["content"])

    def test_add_specific_item(self):
        """test add item with specific item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                get_item_response = self.get_item(item_index, token)
                self.assertEqual(item_name, get_item_response.json()["content"])

    def test_add_item_negative(self):
        """test with invalid token"""
        token = INVALID_TOKEN
        add_item_user_response = self.add_item(item_index, token, item_name)
        self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
        self.assertFalse(add_item_user_response.json()["content"])

    def test_add_item_invalid_index(self):
        """test add item when index not int"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(item_name, token, item_name)
                self.assertNotEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
