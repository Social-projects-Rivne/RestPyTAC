import unittest
import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url

class TestLocked(ApiTestBase):


    def setUp(self):
        """Return admin token"""
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']




    def test_locked(self):
        """Test  functionality of locking users"""
        

    def test_not_locked(self):
        """User should not be locked"""





