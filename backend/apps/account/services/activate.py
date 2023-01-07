from typing import Tuple

import jwt

from django.conf import settings


def decode_token(token: str) -> Tuple[bool, str]:
    email = ""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email = payload["email"]
    except jwt.ExpiredSignatureError:
        print("Token decode signature expired error")
        return (False, email)
    except Exception as e:
        print("Token decode error:", e)
        return (False, email)
    return (True, email)


def activate_user(user):
    user.is_active = True
    user.save()
