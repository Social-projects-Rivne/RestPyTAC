from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, VALID_STATUS_CODE


class TestAllItems(ApiTestBase):

    def test_without_items(self):
        """test when users have not any items"""
        self.reset()
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            get_all_items_response = self.get_all_items(token)
            self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
            self.assertFalse(get_all_items_response.json()["content"])

    def test_with_items(self):
        """test when users have items"""
        self.reset()
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Product")
            self.add_item(2, token, "Car")
            get_all_items_response = self.get_all_items(token)
            self.assertEqual(VALID_STATUS_CODE, get_all_items_response.status_code)
            self.assertNotEqual("", get_all_items_response.json()["content"])
        self.reset()
