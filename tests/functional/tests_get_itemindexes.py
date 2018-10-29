from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES, INVALID_TOKEN


item_name = choice(ITEM_NAMES)
item_index = randint(0, 1000)


class TestGetItemIndexes(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_empty_item_indexes(self):
        """test when user have not item indexes"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                get_item_indexes_response = self.get_itemindexes(token)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertFalse(get_item_indexes_response.json()["content"])

    def test_get_item_indexes(self):
        """test get when user have any item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                get_item_indexes_response = self.get_itemindexes(token)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertTrue(get_item_indexes_response.json()["content"])

    def test_get_item_indexes_by_invalid_token(self):
        """test get item indexes with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                get_item_indexes_response = self.get_itemindexes(INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_item_indexes_response.status_code)
                self.assertFalse(get_item_indexes_response.json()["content"])
