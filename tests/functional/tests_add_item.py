from tests.functional import ApiTestBase
from random import choice, randint
from tests.constants.constants import InitUsers, DefaultToken, VALID_STATUS_CODE, ITEM_NAMES


item_index = randint(0, 1000)
item_name = choice(ITEM_NAMES)


class TestAddItem(ApiTestBase):

    def test_add_item_positive(self):
        """test with valid token"""
        counter = 0
        for user, password in InitUsers.users.items():
            with self.subTest(i=user):
                token = self.login(user, password).json()["content"]
                add_item_user_response = self.add_item(counter, token, item_name)
                counter = counter + 1
                self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
                self.assertTrue(add_item_user_response.json()["content"])
        self.reset()

    def test_add_item_negative(self):
        """test with invalid token"""
        token = DefaultToken.invalid_token
        add_item_user_response = self.add_item(item_index, token, item_name)
        self.assertEqual(VALID_STATUS_CODE, add_item_user_response.status_code)
        self.assertFalse(add_item_user_response.json()["content"])
