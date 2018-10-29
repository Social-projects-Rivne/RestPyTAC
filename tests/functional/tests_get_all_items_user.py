from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, VALID_STATUS_CODE


class TestAllUserItems(ApiTestBase):

    def setUp(self):
        super().setUp()
        self.reset()

    def tearDown(self):
        super().tearDown()
        self.reset()

    def test_get_items_by_admin(self):
        """get user items with admintoken"""
        admintoken = self.login(DefaultUser.user, DefaultUser.password).json()["content"]
        for user in InitUsers.users:
            with self.subTest(i=user):
                get_items_user_response = self.get_user_all_items(user, admintoken)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])

    def test_get_items_by_user(self):
        """get user items with user token"""
        for user in InitUsers.users:
            with self.subTest(i=user):
                token = self.login("kilinatc", "password").json()["content"]
                get_items_user_response = self.get_user_all_items(user, token)
                self.assertEqual(VALID_STATUS_CODE, get_items_user_response.status_code)
                self.assertFalse(get_items_user_response.json()["content"])
