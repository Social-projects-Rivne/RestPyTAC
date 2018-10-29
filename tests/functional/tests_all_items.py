from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, INVALID_TOKEN, VALID_STATUS_CODE


class TestAllItems(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_without_items(self):
        """test when users have not any items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                get_all_items_response = self.get_all_items(token)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertFalse(get_all_items_response.json()["content"])

    def test_with_items(self):
        """test when users have items"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(1, token, "Product")
                self.add_item(2, token, "Car")
                get_all_items_response = self.get_all_items(token)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertNotEqual("", get_all_items_response.json()["content"])
                self.assertTrue(get_all_items_response.json()["content"])

    def test_items_by_invalid_token(self):
        """test with invalid token"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(1, token, "Product")
                self.add_item(2, token, "Car")
                get_all_items_response = self.get_all_items(INVALID_TOKEN)
                self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
                self.assertFalse(get_all_items_response.json()["content"])
