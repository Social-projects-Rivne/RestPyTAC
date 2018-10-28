from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers


class Test(ApiTestBase):
    """test with valid token"""
    def test_add_item_positive(self):
        counter = 1
        for k, v in dict.items(InitUsers.users):
            token = self.login(k, v).json()["content"]
            print(token)
            add_item_user_responce = self.add_item(counter, token, "Product")
            counter = counter + 1
            self.assertEqual(200, add_item_user_responce.status_code)
            self.assertTrue(add_item_user_responce.json()["content"])
        self.reset()

    """test with invalid token"""
    def test_add_item_negative(self):
        token = "2134rfvsd231g45"
        add_item_user_response = self.add_item(1, token, "Car")
        self.assertEqual(200, add_item_user_response.status_code)
        self.assertFalse(add_item_user_response.json()["content"])
