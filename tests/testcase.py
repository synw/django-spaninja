from django.test import TestCase, Client
from main.api import api
from django.contrib.auth import get_user_model
from ninja.testing import TestClient


class NinjaClient(Client, TestClient):
    pass


class NinjaTestCase(TestCase):
    client_class = NinjaClient

    def create_client_helper(self):
        """Create test user and log them to dedicated client."""
        self.user = get_user_model().objects.create_user(
            username="user", password="user"
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin"
        )
        self.user_client = self.client_class(api)
        self.user_client.force_login(self.user)
        self.admin_client = self.client_class(api)
        self.admin_client.force_login(self.admin_user)

    def link_api_helper(self):
        """Can override this method to link another project api to the test case."""
        self.api = api
        self.root_path = self.api.root_path
        self.docs_url = self.api.docs_url

    def setUp(self):
        self.create_client_helper()
        self.link_api_helper()
