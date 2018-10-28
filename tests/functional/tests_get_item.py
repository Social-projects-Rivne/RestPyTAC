from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers


class Test(ApiTestBase):
    """test when users have not items"""
    def test_get_empty_item(self):
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            get_item_response = self.get_item(1, token)
            self.assertEqual(200, get_item_response.status_code)
            self.assertFalse(get_item_response.json()["content"])

    """test when users have item"""
    def test_get_item(self):
        for user, password in dict.items(InitUsers.users):
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Car")
            get_item_response = self.get_item(1, token)
            self.assertEqual(200, get_item_response.status_code)
            self.assertTrue(get_item_response.json()["content"])
        self.reset()