from django.contrib.auth import get_user_model
from django.test import Client, TestCase


PWD = "testpwd"
USERNAME = "testuser"

User = get_user_model()


class AuthViewsTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username=USERNAME, password=PWD)
        self.client = Client()

    def test_auth_logout(self):
        # 200
        self.client.login(username=USERNAME, password=PWD)
        resp = self.client.get("/logout")
        assert resp.status_code == 200  # type: ignore

    def test_auth_login(self):
        # Test 200 OK for valid credentials
        response = self.client.post(
            "/api/account/login",
            data={"username": USERNAME, "password": PWD},
        )
        assert response.status_code == 200  # type: ignore

        self.client.logout()
        # Test 403 Unauthorized for invalid credentials
        response = self.client.post(
            "/api/account/login",
            data={"username": USERNAME, "password": "wrongpassword"},
        )
        assert response.status_code == 403  # type: ignore

        # Test 422 Unprocessable Entity for invalid form data
        response = self.client.post(
            "/api/account/login", data={"username": 3, "password": None}
        )
        assert response.status_code == 422  # type: ignore
