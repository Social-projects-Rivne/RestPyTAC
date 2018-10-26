import unittest
import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url

class TestLocked(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        """Return admin token"""
        response = cls.login(DefaultUser.user, DefaultUser.password)
        cls.adminToken = response.json()['content']




    def test_locked(self):
        """Test  functionality of locking users"""




