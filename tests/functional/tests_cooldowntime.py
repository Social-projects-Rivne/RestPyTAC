import requests

from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, Endpoints
from tests.utils.helper import generate_full_url


class Test(ApiTestBase):

    def test_set_cool_down_time(self):
        """
        Change the cool down time by admin
        :return:
        """
        new_CDT = 500000

        login = self.login(DefaultUser.user, DefaultUser.password)
        token = login.json()["content"]

        # kwargs = {"token": token, "time": new_CDT}
        req = self.change_cool_down_time(token, new_CDT)

        last_req = requests.get(generate_full_url(Endpoints.cooldowntime))
        CDT_after = last_req.json()["content"]

        self.assertEqual(CDT_after, new_CDT)