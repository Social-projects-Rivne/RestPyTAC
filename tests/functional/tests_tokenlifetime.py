"""
Testing response of "/tokenlifetime" module
"""

from tests.constants.constants import DefaultUser
from tests.functional import ApiTestBase
from tests.utils.helper import get_new_value_different_func


class TestTokenLifeTime(ApiTestBase):
    """
    Testing response of "/tokenlifetime"
    """

    def test_get_token_life_time(self):
        """
        Get the value of token life time. If got tlt test pass (positive)
        """

        resp = self.application.get_token_life_time()

        self.assertEqual(resp.status_code, 200)
        # self.assertTrue(resp.json()["content"] or resp.json()["content"] == 0)
        self.assertTrue(resp.json()["content"])

    def test_set_token_life_time_admin_positive(self):
        """
        Change the token life time value by admin (200000). If tlt changed test pass (positive)
        """

        new_tlt = get_new_value_different_func(self.application.get_token_life_time, 200000, 100000)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(tlt_after, new_tlt)

    def test_set_token_life_time_admin_negative(self):
        """
        Change the token life time value by admin (-200000). If tft not changed test pass (negative)
        """

        new_tlt = get_new_value_different_func(self.application.get_token_life_time, -200000, -100000)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertNotEqual(tlt_after, new_tlt)

    def test_set_token_life_time_admin_zero(self):
        """
        Change the token life time value by admin (zero). If tlt changed test pass (positive)
        """

        new_tlt = get_new_value_different_func(self.application.get_token_life_time, 0, 0)

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertNotEqual(tlt_after, new_tlt)

    def test_set_token_life_time_admin_none(self):
        """
        Change the token life time value by admin (None). If tlt stand 1000 (default value) test pass (negative)
        """

        new_tlt = None
        def_tlt = 1000

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(tlt_after, def_tlt)

    def test_set_token_life_time_admin_float(self):
        """
        Change the token life time value by admin (float 200000.555). If tlt didn't change test pass (negative)
        """

        new_tlt = get_new_value_different_func(self.application.get_token_life_time, 200000.555, 100000)

        resp = self.application.get_token_life_time()
        curr_tlt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(tlt_after, curr_tlt)

    def test_set_token_life_time_admin_text(self):
        """
        Change the token life time value by admin (text). If tlt didn't change test pass (negative)
        """

        new_tlt = "f%kdm525!("

        resp = self.application.get_token_life_time()
        curr_tlt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(tlt_after, curr_tlt)

    def test_set_token_life_time_user(self):
        """
        Change the token life time value by user (without admin rights). If tlt didn't change test pass (negative)
        """

        new_tlt = get_new_value_different_func(self.application.get_token_life_time, 500000, 100000)

        resp = self.application.get_token_life_time()
        curr_tlt = resp.json()["content"]

        login = self.application.login(DefaultUser.user_akimatc, DefaultUser.password_akimatc)
        token = login.json()["content"]

        resp = self.application.change_token_life_time(token, new_tlt)

        last_resp = self.application.get_token_life_time()
        tlt_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.json()["content"])
        self.assertEqual(tlt_after, curr_tlt)
