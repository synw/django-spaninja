from typing import Tuple
from django.contrib.auth import get_user_model
from django.middleware.csrf import get_token
from django.http import HttpRequest
from django.contrib.auth import authenticate, logout, login

from ninja import Router

from django.contrib.auth.forms import AuthenticationForm
from apps.account.forms.registration import RegistrationForm
from apps.account.utils.token import decode_token
from apps.account.utils.email import email_activation_token

from apps.base.schemas import (
    MsgResponseContract,
    FormInvalidResponseContract,
)
from apps.account.schemas import (
    LoginFormContract,
    RegisterFormContract,
    StateContract,
)


router = Router(tags=["account"])


@router.post(
    "/register",
    auth=None,
    response={
        200: None,
        422: FormInvalidResponseContract,
    },
)
def register_save(request: HttpRequest, data: RegisterFormContract):
    """Register a user from a registration form

    Endpoint url: /api/account/register

    Args:
        request (HttpRequest): the django http request object
        data (RegisterFormContract): the form json payload

    Returns:
        HttpResponse: an http response

    Example:
        ::

        # example of valid payload
        {
            "name": "John Doe",
            "email": "mymail@example.com",
            "password1": "xxxzzzxxx",
            "password2": "xxxzzzxxx",
        }

        # example of form error payload return with a 422 status code
        {
            "errors": {
                'password2': [
                    {
                        'message': 'The two password fields didn’t match.',
                        'code': 'password_mismatch'
                    }
                ]
            }
        }
    """
    form = RegistrationForm(data=data.dict())
    if not form.is_valid():
        return 422, {"errors": form.errors.get_json_data(escape_html=True)}

    user = form.save()
    email_data = {
        "request": request,
        "user": user,
        "to_email": form.cleaned_data.get("email"),
        "subject": "Activate your account.",
        "template": "active_email.html",
    }
    email_activation_token(**email_data)
    return 200, None


@router.get(
    "/activate/{token}",
    auth=None,
    response={
        200: None,
        204: None,
        401: MsgResponseContract,
    },
    url_name="activate",
)
def activate_save(
    request: HttpRequest, token: str
) -> Tuple[int, None | MsgResponseContract]:
    """Activate a user from a token

    Endpoint url: /api/account/activate/{token}

    User has clicked on link in an email with an activation token, \
    and we activate the user if the token is valid

    Args:
        request (HttpRequest): the django http request object
        token (str): the token

    Returns:
        Tuple[int, None | MsgResponseContract]: a 204 empty or a 401 with a message if \
        the token is invalid

    Example:
        ::

        # example of an activation refused with a 401 http status code
        {
            "message": "Account activation refused"
        }
    """
    is_valid, email = decode_token(token)
    if is_valid is False:
        return 401, MsgResponseContract(**{"message": "Account activation refused"})
    user = get_user_model().objects.get(email=email)
    if user:
        user.is_active = True
        user.save()
        return 204, None
    return 401, MsgResponseContract(**{"message": "Account activation refused"})


@router.post(
    "/login",
    auth=None,
    response={
        200: None,
        422: FormInvalidResponseContract,
        401: MsgResponseContract,
    },
)
def authlogin(
    request: HttpRequest, data: LoginFormContract
) -> Tuple[int, None | FormInvalidResponseContract | MsgResponseContract]:
    """Login a user from a username and password payload

    Endpoint url: /api/account/login

    Args:
        request (HttpRequest): the django http request object
        data (LoginFormContract): the username and password payload

    Returns:
        Tuple[int, None | FormInvalidResponseContract | MsgResponseContract]:
        the http status code and the data payload
    """
    form = AuthenticationForm(data=data.dict())
    if form.is_valid() is False:
        return 422, FormInvalidResponseContract.parse_obj(
            {"errors": form.errors.get_json_data(escape_html=True)}
        )

    user = authenticate(
        username=form.cleaned_data.get("username"),
        password=form.cleaned_data.get("password"),
    )
    if user is not None:
        login(request, user)  # returns a 200
        return 200, None
    else:
        return 401, MsgResponseContract(**{"message": "Login refused"})


@router.get(
    "/logout",
    response={200: None, 403: None},
)
def authlogout(request: HttpRequest) -> Tuple[int, None]:
    """Logout a user

    Endpoint url: /api/account/logout

    Args:
        request (HttpRequest): the django http request object

    Returns:
        Tuple[int, None]: the http status code and None
    """
    if request.user.is_anonymous is True:
        return 403, None
    logout(request)  # returns a 200
    return 200, None


@router.get("/state", auth=None, response={200: StateContract})
def global_state(request: HttpRequest) -> Tuple[int, StateContract]:
    """Returns info on user state and set a csrf token

    Endpoint url: /api/account/state

    Args:
        request (HttpRequest): the django http request object

    Returns:
        Tuple[int, StateContract]: the http status code and the data payload
    """
    out = {"is_connected": False, "username": "anonymous"}
    if request.user.is_anonymous is False:
        out["is_connected"] = True
        out["username"] = request.user.get_username()
    # set a csrf token cookie
    get_token(request)
    return 200, StateContract(**out)
