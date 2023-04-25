from django.contrib.auth import get_user_model

from apps.account.utils.token import encode_token
from main.api import api
from ..testcase import NinjaTestCase
import json

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
        self.assertJSONEqual(
            response.content, {"is_connected": False, "username": "anonymous"}
        )

    def test_user_account_state(self):
        response = self.user_client.get(f"{api.root_path}account/state")
        assert response.status_code == 200
        self.assertJSONEqual(
            response.content, {"is_connected": True, "username": "user"}
        )

    def test_admin_account_state(self):
        response = self.admin_client.get(f"{api.root_path}account/state")
        assert response.status_code == 200
        assert response.content == b'{"is_connected": true, "username": "admin"}'

    def test_accout_register(self):
        response = self.client.post(
            f"{api.root_path}account/register",
            data=json.dumps(
                {
                    "name": "johndoe",  # TODO: name is not used, may change username django settings
                    "password1": "johndoeknowall",
                    "password2": "johndoeknowall",
                    "email": "johndoe@dummy.dummy",
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == 200
        joker_user = get_user_model().objects.get(username="johndoe@dummy.dummy")
        assert joker_user

    def test_accout_register_fail(self):
        response = self.client.post(
            f"{api.root_path}account/register",
            data=json.dumps(
                {
                    "name": "johndoe",
                    "password1": "johndoeknowall",
                    "password2": "jokerknowall",
                    "email": "johndoe@dummy.dummy",
                }
            ),
            content_type="application/json",
        )
        assert response.status_code == 422
        assert response.json() == {
            "errors": {
                "password2": [
                    {
                        "code": "password_mismatch",
                        "message": "The two passwords you filled out do not " "match.",
                    }
                ]
            }
        }

    def test_account_activate_token(self):
        self.client.post(
            f"{api.root_path}account/register",
            data=json.dumps(
                {
                    "name": "johndoe",  # TODO: name is not used, may change username django settings
                    "password1": "johndoeknowall",
                    "password2": "johndoeknowall",
                    "email": "johndoe@dummy.dummy",
                }
            ),
            content_type="application/json",
        )
        # Get token
        user = get_user_model().objects.get(username="johndoe@dummy.dummy")
        token = encode_token(user.email)
        # Activate
        assert user.is_active is False
        response = self.client.get(f"{api.root_path}account/activate/{token}")
        assert response.status_code == 204
        assert response.reason_phrase == "No Content"
        user.refresh_from_db()
        assert user.is_active

    def test_account_activate_token_fail(self):
        response = self.client.get(f"{api.root_path}account/activate/invalidtoken")
        assert response.status_code == 401
        assert response.json() == {"message": "Account activation refused"}
