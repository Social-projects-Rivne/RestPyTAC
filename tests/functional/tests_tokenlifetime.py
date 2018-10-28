from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class TestTokenLifeTime(ApiTestBase):

    def test_get_token_life_time(self):
        """
        Get the value of token life time
        :return:
        """

        req = self.get_token_life_time()

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.ok)
        self.assertTrue(req.json()["content"] or req.json()["content"] == 0)

    def test_set_token_life_time_admin_positive(self):
        """
        Change the token life time value by admin (positive)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = self.get_new_token_life_time(200000, 100000)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_negative(self):
        """
        Change the token life time value by admin (negative)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = self.get_new_token_life_time(-200000, -100000)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_zero(self):
        """
        Change the token life time value by admin (zero)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = self.get_new_token_life_time(0, 0)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(TLT_after, new_TLT)

    def test_set_token_life_time_admin_none(self):
        """
        Change the token life time value by admin (None)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = None
        def_TLT = 1000

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(TLT_after, def_TLT)

    def test_set_token_life_time_admin_float(self):
        """
        Change the token life time value by admin (float)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = self.get_new_token_life_time(200000.555, 100000)

        req = self.get_token_life_time()
        curr_TLT = req.json()["content"]

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 400)
        self.assertFalse(req.ok)
        self.assertEqual(TLT_after, curr_TLT)

    def test_set_token_life_time_admin_text(self):
        """
        Change the token life time value by admin (text)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = "f%kdm525!("

        req = self.get_token_life_time()
        curr_TLT = req.json()["content"]

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 400)
        self.assertFalse(req.ok)
        self.assertEqual(TLT_after, curr_TLT)

    def test_set_token_life_time_user(self):
        """
        Change the token life time value by user (without admin rights)
        :return:
        """

        # must use, because after et_token_life_time = 0, admin logout
        self.get_reset()

        new_TLT = self.get_new_token_life_time(500000, 100000)

        req = self.get_token_life_time()
        curr_TLT = req.json()["content"]

        login = self.login(DefaultUser.user, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_token_life_time(token, new_TLT)

        last_req = self.get_token_life_time()
        TLT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertFalse(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(TLT_after, curr_TLT)

    def get_new_token_life_time(self, new_TLT, step):
        """
        Get new token life time (TLT) value.
        If current TLT equal new value then we make greater new TLT by step
        :return:
        """

        req = self.get_token_life_time()
        curr_TLT = req.json()["content"]

        if curr_TLT == new_TLT:
            new_TLT = curr_TLT + step

        return new_TLT