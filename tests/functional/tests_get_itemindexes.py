from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, VALID_STATUS_CODE


class Test(ApiTestBase):
    def test_get_empty_itemindexes(self):
        self.reset()
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            get_itemindexes_response = self.get_itemindexes(token)
            self.assertEqual(VALID_STATUS_CODE, get_itemindexes_response.status_code)
            self.assertEqual("", get_itemindexes_response.json()["content"])

    def test_get_itemindexes(self):
        self.reset()
        for user, password in InitUsers.users.items():
            token = self.login(user, password).json()["content"]
            self.add_item(3, token, "Product")
            get_itemindexes_response = self.get_itemindexes(token)
            self.assertEqual(VALID_STATUS_CODE, get_itemindexes_response.status_code)
            self.assertNotEqual("", get_itemindexes_response.json()["content"])
            self.assertEqual("3 ", get_itemindexes_response.json()["content"])
        self.reset()
