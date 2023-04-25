from .testcase import NinjaTestCase


class TestNinjaTestCase(NinjaTestCase):
    def test_get_public(self):
        res = self.client.get("/")
        assert res.status_code == 200

    def test_get_anonymous(self):
        res = self.client.get(f"{self.root_path}{self.docs_url[1:]}")
        assert res.status_code == 302

    def test_get_authentificated(self):
        self.client.force_login(self.user)
        res_redirect = self.client.get(f"{self.root_path}{self.docs_url[1:]}")
        assert res_redirect.status_code == 302
        res = self.client.get(f"{self.root_path}login")
        assert res.status_code == 200

    def test_get_admin_authentificated(self):
        self.client.force_login(self.admin_user)
        res = self.client.get(f"{self.root_path}{self.docs_url[1:]}")
        assert res.status_code == 200
