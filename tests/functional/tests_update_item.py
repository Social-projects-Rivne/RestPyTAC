from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, VALID_STATUS_CODE


class Test(ApiTestBase):

    def test_update_empty_item(self):
        """test update item when user has no item"""
        self.reset()
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            update_item_response = self.update_item(1, token, "Product")
            self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
            self.assertFalse(update_item_response.json()["content"])

    def test_update_item(self):
        """test update item when user has item"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Car")
            update_item_response = self.update_item(1, token, "Product")
            self.assertEqual(VALID_STATUS_CODE, update_item_response.status_code)
            self.assertTrue(update_item_response.json()["content"])
        self.reset()
