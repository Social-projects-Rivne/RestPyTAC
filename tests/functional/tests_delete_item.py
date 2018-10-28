from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers


class Test(ApiTestBase):
    """delete when users have not any items"""
    def test_delete_empty_item(self):
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            delete_item_response = self.delelete_item(1, token)
            self.assertEqual(200, delete_item_response.status_code)
            self.assertFalse(delete_item_response.json()["content"])

    """delete when user has item"""
    def test_delete_item(self):
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Product")
            delete_item_response = self.delelete_item(1, token)
            self.assertEqual(200, delete_item_response.status_code)
            self.assertTrue(delete_item_response.json()["content"])
