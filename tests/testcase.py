from django.test import TestCase
from main.api import api
from django.contrib.auth import get_user_model


class NinjaTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user", password="user"
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin"
        )
        self.user_client = self.client_class()
        self.user_client.force_login(self.user)

        self.admin_client = self.client_class()
        self.admin_client.force_login(self.admin_user)

    def test_get_public(self):
        res = self.client.get("/")
        assert res.status_code == 200

    def test_get_anonymouss(self):
        res = self.client.get(f"{api.root_path}{api.docs_url[1:]}")
        assert res.status_code == 302

    def test_get_authentificated(self):
        self.client.force_login(self.user)
        res_redirect = self.client.get(f"{api.root_path}{api.docs_url[1:]}")
        assert res_redirect.status_code == 302
        res = self.client.get(f"{api.root_path}login")
        assert res.status_code == 200

    def test_get_admin_authentificated(self):
        self.client.force_login(self.admin_user)
        res = self.client.get(f"{api.root_path}{api.docs_url[1:]}")
        assert res.status_code == 200
