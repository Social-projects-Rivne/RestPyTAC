from tests.functional import ApiTestBase


class Test(ApiTestBase):
        """get user items with admintoken"""
        def test_item(self):
            login = self.login("admin", "qwerty")
            get_items_user = self.getUserItems(login.json()["content"])
            print(get_items_user.content)
            self.assertEqual(200, get_items_user.status_code)
            self.assertEqual("", get_items_user.json()["content"])

        """get user items with user token"""
        def test_items(self):
            login = self.login("kilinatc", "qwerty")
            get_items_user = self.getUserItems(login.json()["content"])
            print(get_items_user.content)
            self.assertEqual(200, get_items_user.status_code)
            self.assertEqual("", get_items_user.json()["content"])
