from tests.functional import ApiTestBase
from tests.constants.constants import DefaultUser


class Test(ApiTestBase):

    def test_get_cool_down_time(self):
        """
        Get the value of cool down time
        :return:
        """

        req = self.get_cool_down_time()

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.ok)
        self.assertTrue(req.json()["content"] or req.json()["content"] == 0)

    def test_set_cool_down_time_admin_positive(self):
        """
        Change the cool down time value by admin (positive)
        :return:
        """

        new_CDT = self.get_new_cool_down_time(200000, 100000)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_negative(self):
        """
        Change the cool down time value by admin (negative)
        :return:
        """

        new_CDT = self.get_new_cool_down_time(-200000, -100000)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_zero(self):
        """
        Change the cool down time value by admin (zero)
        :return:
        """

        new_CDT = self.get_new_cool_down_time(0, 0)

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(CDT_after, new_CDT)

    def test_set_cool_down_time_admin_none(self):
        """
        Change the cool down time value by admin (None)
        :return:
        """

        new_CDT = None
        def_CDT = 1000

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 200)
        self.assertTrue(req.json()["content"])
        self.assertTrue(req.ok)
        self.assertEqual(CDT_after, def_CDT)

    def test_set_cool_down_time_admin_float(self):
        """
        Change the cool down time value by admin (float)
        :return:
        """

        new_CDT = self.get_new_cool_down_time(200000.555, 100000)

        req = self.get_cool_down_time()
        curr_CDT = req.json()["content"]

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 400)
        self.assertFalse(req.ok)
        self.assertEqual(CDT_after, curr_CDT)

    def test_set_cool_down_time_admin_text(self):
        """
        Change the cool down time value by admin (text)
        :return:
        """

        new_CDT = "f%kdm525!("

        req = self.get_cool_down_time()
        curr_CDT = req.json()["content"]

        login = self.login(DefaultUser.admin, DefaultUser.password)
        token = login.json()["content"]

        req = self.change_cool_down_time(token, new_CDT)

        last_req = self.get_cool_down_time()
        CDT_after = last_req.json()["content"]

        self.assertEqual(req.status_code, 400)
        self.assertFalse(req.ok)
        self.assertEqual(CDT_after, curr_CDT)

    def test_set_cool_down_time_user(self):
        """
        Change the cool down time value by user (without admin rights)
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
        self.assertTrue(req.ok)
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