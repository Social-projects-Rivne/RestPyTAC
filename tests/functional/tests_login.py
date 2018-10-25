import requests

from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers

class Test(ApiTestBase):

    def test_login(self):
        # sceleton, not refactoring
        login = self.login("admin", "qwerty")
        self.assertEquals(200, login.status_code)
