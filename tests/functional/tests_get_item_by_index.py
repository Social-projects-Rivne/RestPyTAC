from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, VALID_STATUS_CODE


class Test(ApiTestBase):

    def test_get_empty_item(self):
        """test when users have not items"""
        self.reset()
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                get_item_response = self.get_item(1, token)
                self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
                self.assertFalse(get_item_response.json()["content"])

    def test_get_item(self):
        """test when users have item"""
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(1, token, "Car")
            get_item_response = self.get_item(1, token)
            self.assertEqual(VALID_STATUS_CODE, get_item_response.status_code)
            self.assertTrue(get_item_response.json()["content"])
            self.assertEqual("Car", get_item_response.json()["content"])
        self.reset()
