import requests

from tests.functional import ApiTestBase
from tests.constants.constants import InitUsers, DefaultUser, Endpoints
from tests.utils.helper import generate_full_url


class Test(ApiTestBase):

    def test_set_cool_down_time_admin(self):
        """
        Change the cool down time by admin
        :return:
        """
        new_CDT = self.get_new_cool_down_time(200000, 100000)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(CDT_after, new_CDT)
        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])

    def test_set_cool_down_time_user(self):
        """
        Change the cool down time by user (without admin rights)
        :return:
        """
        new_CDT = self.get_new_cool_down_time(500000, 100000)

        req = self.get_cool_down_time()
        curr_CDT = req.json()["content"]

        login = self.login(DefaultUser.user, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertFalse(req.json()["content"])
        self.assertEqual(CDT_after, curr_CDT)

    def get_new_cool_down_time(self, new_CDT, step):
        """
        Get new cool down time (CDT) value.
        If current CDT equal new value then we make greater new CDT by step
        :return:
        """
        req = self.get_cool_down_time()
        curr_CDT = req.json()["content"]

        if curr_CDT == new_CDT:
            new_CDT = curr_CDT + step

        return new_CDT
