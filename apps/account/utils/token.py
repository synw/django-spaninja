from typing import Tuple

import jwt

from django.conf import settings


def decode_token(token: str) -> Tuple[bool, str]:
    """
    Decodes and validates an activation token.
    Args:
        token (str): The token to decode and validate.

    Returns:
        Tuple[bool, str]: A tuple where the first element indicates if
                           the token is valid and the second element contains
                           the user email.
    """
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


def encode_token(email: str) -> str:
    """Encode a token

    Args:
        email (str): the email to encode

    Returns:
        str: the encoded token
    """
    return jwt.encode({"email": email}, settings.SECRET_KEY, algorithm="HS256")
