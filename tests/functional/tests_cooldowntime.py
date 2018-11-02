"""
Testing response of "/cooldowntime" module
"""

from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser
from tests.utils.helper import get_new_value_different_func


class TestCoolDownTime(ApiTestBase):
    """
    Testing response of "/cooldowntime"
    """

    def test_get_cool_down_time(self):
        """
        Get the value of cool down time
        """

        resp = self.application.get_cool_down_time()

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"] or resp.json()["content"] == 0)

    def test_set_cool_down_time_admin_positive(self):
        """
        Change the cool down time value by admin (positive)
        """

        new_cdt = get_new_value_different_func(self.application.get_cool_down_time, 200000, 100000)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(cdt_after, new_cdt)

    def test_set_cool_down_time_admin_negative(self):
        """
        Change the cool down time value by admin (negative)
        """

        new_cdt = get_new_value_different_func(self.application.get_cool_down_time, -200000, -100000)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(cdt_after, new_cdt)

    def test_set_cool_down_time_admin_zero(self):
        """
        Change the cool down time value by admin (zero)
        """

        new_cdt = get_new_value_different_func(self.application.get_cool_down_time, 0, 0)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(cdt_after, new_cdt)

    def test_set_cool_down_time_admin_none(self):
        """
        Change the cool down time value by admin (None)
        """

        new_cdt = None
        def_cdt = 1000

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(cdt_after, def_cdt)

    def test_set_cool_down_time_admin_float(self):
        """
        Change the cool down time value by admin (float)
        """

        new_cdt = get_new_value_different_func(self.application.get_cool_down_time, 200000.555, 100000)

        resp = self.application.get_cool_down_time()
        curr_cdt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(cdt_after, curr_cdt)

    def test_set_cool_down_time_admin_text(self):
        """
        Change the cool down time value by admin (text)
        """

        new_cdt = "f%kdm525!("

        resp = self.application.get_cool_down_time()
        curr_cdt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(cdt_after, curr_cdt)

    def test_set_cool_down_time_user(self):
        """
        Change the cool down time value by user (without admin rights)
        """

        new_cdt = get_new_value_different_func(self.application.get_cool_down_time, 500000, 100000)

        resp = self.application.get_cool_down_time()
        curr_cdt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_akimatc, DefaultUser.password_akimatc)
        token = login.json()["content"]

        resp = self.application.change_cool_down_time(token, new_cdt)

        last_resp = self.application.get_cool_down_time()
        cdt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.json()["content"])
        self.assertEqual(cdt_after, curr_cdt)
