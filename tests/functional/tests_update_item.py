from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers


class Test(ApiTestBase):
    """test update item when users has no item"""
    def test_update_empty_item(self):
        self.reset()
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            update_item_response = self.update_item(1, token, "Product")
            self.assertEqual(200, update_item_response.status_code)
            self.assertFalse(update_item_response.json()["content"])

    """test update item when users have item"""
    def test_update_item(self):
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Car")
            update_item_response = self.update_item(1, token, "Product")
            self.assertEqual(200, update_item_response.status_code)
            self.assertTrue(update_item_response.json()["content"])
        self.reset()
