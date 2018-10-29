import requests

from tests.functional import ApiTestBase
from tests.constants.constants import Endpoints, DefaultUser
from tests.utils.helper import generate_full_url


class TestRemoveUser(ApiTestBase):

    def setUp(self):
        super().setUp()
        response = self.login(DefaultUser.user, DefaultUser.password)
        self.adminToken = response.json()['content']

    def test_remove_User_with_valid_data(self):
        # create test_user
        creating = requests.post(generate_full_url(Endpoints.user), params={'token': self.adminToken, "name": "testuserdelete",
                                                                 "password": "qwerty", "rights": "false"})
        print (creating.json())
        #delete test user
        remove_created_user = requests.delete(generate_full_url(Endpoints.user),
                                            params={'token': self.adminToken, "name": "testuserdelete"})
        print(remove_created_user.json())
        self.assertIn("true", remove_created_user.text)

        try to login with deleted user
    def test_login_deleted_user(self):
        deleted_user_login = requests.post(generate_full_url(Endpoints.login),
                                            params = {"name": "testuserdelete", "password": "qwerty"})
        self.assertIn("ERROR", deleted_user_login.text, "Error, user not deleted")


