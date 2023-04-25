from django.test import TestCase
from main.api import api
from django.contrib.auth import get_user_model


class NinjaTestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = get_user_model().objects.create_user(
            username="user", password="user"
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin"
        )
        # Create test client
        self.user_client = self.client_class()
        self.user_client.force_login(self.user)
        self.admin_client = self.client_class()
        self.admin_client.force_login(self.admin_user)
        # Link api
        self.api = api
        self.root_path = self.api.root_path
        self.docs_url = self.api.docs_url
