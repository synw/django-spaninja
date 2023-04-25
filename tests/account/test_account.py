from django.contrib.auth import get_user_model
from main.api import api
from ..testcase import NinjaTestCase


PWD = "testpwd"
USERNAME = "testuser"


def test_user_creation():
    User = get_user_model()
    user = User.objects.create(username=USERNAME, password=PWD)
    assert user


def test_admin_account_state(admin_client):
    response = admin_client.get(f"{api.root_path}account/state")
    assert response.status_code == 200
    assert response.content == b'{"is_connected": true, "username": "admin"}'


class TestAccount(NinjaTestCase):
    def test_anonymous_account_state(self):
        response = self.client.get(f"{api.root_path}account/state")
        assert response.status_code == 200
        assert response.content == b'{"is_connected": false, "username": "anonymous"}'

    def test_user_account_state(self):
        response = self.user_client.get(f"{api.root_path}account/state")
        assert response.status_code == 200
        assert response.content == b'{"is_connected": true, "username": "user"}'

    def test_admin_account_state(self):
        response = self.admin_client.get(f"{api.root_path}account/state")
        assert response.status_code == 200
        assert response.content == b'{"is_connected": true, "username": "admin"}'
