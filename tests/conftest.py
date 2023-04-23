import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture()
def visitor(django_user_model):
    return django_user_model.objects.create(username="visitor", password="visitor")


@pytest.fixture()
def staff(django_user_model):
    return django_user_model.objects.create(
        username="staff", password="staff", is_staff=True, is_superuser=False
    )


@pytest.fixture()
def administrator(django_user_model):
    return django_user_model.objects.create(
        username="administrator",
        password="administrator",
        is_staff=True,
        is_superuser=True,
    )
