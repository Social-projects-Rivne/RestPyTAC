from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES


item_index = randint(0, 1000)
item_name = choice(ITEM_NAMES)


class TestGetItemByIndex(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_empty_item(self):
        """test when users have not items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                get_item_response = self.get_item(item_index, token)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertFalse(get_item_response.json()["content"])

    def test_get_item(self):
        """test when users have item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                get_item_response = self.get_item(item_index, token)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertTrue(get_item_response.json()["content"])
                self.assertEqual(item_name, get_item_response.json()["content"])

    def test_get_item_index_str(self):
        """test get item with str index"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                get_item_response = self.get_item("call", token)
                self.assertNotEqual(VALID_STATUS_CODE, get_item_response.status_code)
