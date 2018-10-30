from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser
from tests.utils.helper import get_new_value_different_func


class TestTokenLifeTime(ApiTestBase):
    """
    Testing response of "/tokenlifetime"
    """

    def test_get_token_life_time(self):
        """
        Get the value of token life time
        """

        resp = self.get_token_life_time()

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"] or resp.json()["content"] == 0)

    def test_set_token_life_time_admin_positive(self):
        """
        Change the token life time value by admin (positive)
        """

        # must use, because after get_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = get_new_value_different_func(self.get_token_life_time, 200000, 100000)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_negative(self):
        """
        Change the token life time value by admin (negative)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = get_new_value_different_func(self.get_token_life_time, -200000, -100000)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_zero(self):
        """
        Change the token life time value by admin (zero)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = get_new_value_different_func(self.get_token_life_time, 0, 0)

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_none(self):
        """
        Change the token life time value by admin (None)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = None
        def_TLT = 1000

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()["content"])
        self.assertEqual(TLT_after, def_TLT)

    def test_set_token_life_time_admin_float(self):
        """
        Change the token life time value by admin (float)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = get_new_value_different_func(self.get_token_life_time, 200000.555, 100000)

        resp = self.get_token_life_time()
        curr_TLT = resp.json()["content"]

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(TLT_after, curr_TLT)

    def test_set_token_life_time_admin_text(self):
        """
        Change the token life time value by admin (text)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = "f%kdm525!("

        resp = self.get_token_life_time()
        curr_TLT = resp.json()["content"]

        login = self.login(DefaultUser.user_admin, DefaultUser.password_admin)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(TLT_after, curr_TLT)

    def test_set_token_life_time_user(self):
        """
        Change the token life time value by user (without admin rights)
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = get_new_value_different_func(self.get_token_life_time, 500000, 100000)

        resp = self.get_token_life_time()
        curr_TLT = resp.json()["content"]

        login = self.login(DefaultUser.user_akimatc, DefaultUser.password_akimatc)
        token = login.json()["content"]

        resp = self.change_token_life_time(token, new_TLT)

        last_resp = self.get_token_life_time()
        TLT_after = last_resp.json()["content"]

        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.json()["content"])
        self.assertEqual(TLT_after, curr_TLT)
