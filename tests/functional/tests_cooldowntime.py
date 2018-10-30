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

        resp = self.get_cool_down_time()

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"] or resp.json()["content"] == 0)

    def test_set_cool_down_time_admin_positive(self):
        """
        Change the cool down time value by admin (positive)
        """

        new_CDT = get_new_value_different_func(self.get_cool_down_time, 200000, 100000)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_negative(self):
        """
        Change the cool down time value by admin (negative)
        """

        new_CDT = get_new_value_different_func(self.get_cool_down_time, -200000, -100000)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_zero(self):
        """
        Change the cool down time value by admin (zero)
        """

        new_CDT = get_new_value_different_func(self.get_cool_down_time, 0, 0)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_none(self):
        """
        Change the cool down time value by admin (None)
        """

        new_CDT = None
        def_CDT = 1000

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(CDT_after, def_CDT)

    def test_set_cool_down_time_admin_float(self):
        """
        Change the cool down time value by admin (float)
        """

        new_CDT = get_new_value_different_func(self.get_cool_down_time, 200000.555, 100000)

        resp = self.get_cool_down_time()
        curr_CDT = resp.json()["content"]

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(CDT_after, curr_CDT)

    def test_set_cool_down_time_admin_text(self):
        """
        Change the cool down time value by admin (text)
        """

        new_CDT = "f%kdm525!("

        resp = self.get_cool_down_time()
        curr_CDT = resp.json()["content"]

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(CDT_after, curr_CDT)

    def test_set_cool_down_time_user(self):
        """
        Change the cool down time value by user (without admin rights)
        """

        new_CDT = get_new_value_different_func(self.get_cool_down_time, 500000, 100000)

        resp = self.get_cool_down_time()
        curr_CDT = resp.json()["content"]

        login = self.login(DefaultUser.user_akimatc, DefaultUser.password_akimatc)
        token = login.json()["content"]

        resp = self.change_cool_down_time(token, new_CDT)

        last_resp = self.get_cool_down_time()
        CDT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.json()["content"])
        self.assertEqual(CDT_after, curr_CDT)
