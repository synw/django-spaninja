from django.test import TestCase
from main.api import api


class NinjaTestCase(TestCase):
    def test_get_public(self):
        res = self.client.get("/")
        assert res.status_code == 200

    def test_get_unauthentificated(self):
        res = self.client.get(f"{api.root_path}docs")
        assert res.status_code == 302
