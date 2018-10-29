from tests.functional import ApiTestBase
from random import randint, choice
from tests.constants.constants import InitUsers, VALID_STATUS_CODE, ITEM_NAMES


item_name = choice(ITEM_NAMES)
item_index = randint(0, 1000)


class Test(ApiTestBase):

    def test_delete_empty_item(self):
        """delete when users have not any items"""
        self.reset()
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                delete_item_response = self.delete_item(item_index, token)
                self.assertEqual(VALID_STATUS_CODE, delete_item_response.status_code)
                self.assertFalse(delete_item_response.json()["content"])

    def test_delete_item(self):
        """delete when user has item"""
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                self.add_item(item_index, token, item_name)
                delete_item_response = self.delete_item(item_index, token)
                self.assertEqual(VALID_STATUS_CODE, delete_item_response.status_code)
                self.assertTrue(delete_item_response.json()["content"])
        self.reset()
