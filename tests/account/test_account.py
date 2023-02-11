from django.contrib.auth import get_user_model


PWD = "testpwd"
USERNAME = "testuser"


def test_user_creation():
    User = get_user_model()
    user = User.objects.create(username=USERNAME, password=PWD)
    assert user
