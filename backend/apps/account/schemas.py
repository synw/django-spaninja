from typing import Union

from ninja import Schema


class LoginFormContract(Schema):
    """Incoming data from login form post"""

    username: Union[str, None]
    password: Union[str, None]


class RegisterFormContract(Schema):
    """Incoming data from registration form post"""

    name: Union[str, None]
    email: Union[str, None]
    password1: Union[str, None]
    password2: Union[str, None]


class StateContract(Schema):
    """Account state data"""

    is_connected: bool
    username: str
