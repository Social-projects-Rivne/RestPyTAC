"""
Functional tests for admins
"""

from tests.constants.constants import DefaultUser, Endpoints
from tests.functional import ApiTestBase
from tests.utils.helper import generate_full_url


class TestAdmins(ApiTestBase):

    def check_status_code_200(self, status_code: int):
        self.assertEqual(status_code, 200, "Error response status code (expected 200)")

    def test_admins(self):
        """Get all admins with admin token. If list not empty test pass"""
        login = self.login(DefaultUser.user, DefaultUser.password)
        self.check_status_code_200(login.status_code)
        # print(login.text)
        token = login.json()
        token["token"] = token.pop("content")
        all_admins = self.request_session.get(generate_full_url(Endpoints.admins), params=token)
        self.check_status_code_200(all_admins.status_code)
        # print(all_admins.text)
        self.assertTrue(all_admins.json().get("content"), "Content is empty")

    def test_admins_users(self):
        """Get all admins without admin token. If list empty test pass"""
        for user, password in users.items():
            login = self.login(user, password)
            self.check_status_code_200(login.status_code)
            # print(login.text)
            token = login.json()
            token["token"] = token.pop("content")
            all_admins = self.request_session.get(generate_full_url(Endpoints.admins), params=token)
            self.check_status_code_200(all_admins.status_code)
            # print(all_admins.text)
            self.assertFalse(all_admins.json().get("content"), "Content is not empty")


users = {"akimatc": "qwerty",
         "khalaktc": "qwerty",
         "kilinatc": "qwerty",
         "OKonokhtc": "qwerty",
         "otlumtc": "qwerty",
         "slototc": "qwerty",
         "vbudktc": "qwerty",
         "vvasylystc": "qwerty"}
