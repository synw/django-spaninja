from django.contrib.auth import get_user_model
from django.middleware.csrf import get_token
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, logout, login

from ninja import Router

from django.contrib.auth.forms import AuthenticationForm
from backend.apps.account.forms.registration import RegistrationForm
from backend.apps.account.services.activate import decode_token, activate_user
from backend.apps.account.services.email import email_activation_token

from ...base.schemas import (
    MsgResponseContract,
    FormInvalidResponseContract,
)
from backend.apps.account.schemas import (
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
def register_save(
    request: HttpRequest, response: HttpResponse, data: RegisterFormContract
):
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
def activate_save(request: HttpRequest, response: HttpResponse, token: str):
    """User has clicked on link with token, and can now login"""
    is_valid, email = decode_token(token)
    if is_valid is False:
        return 401, {"message": "Account activation refused"}
    user = get_user_model().objects.get(email=email)
    if user:
        activate_user(user)
        return 204
    return 401, {"message": "Account activation refused"}


@router.post(
    "/login",
    auth=None,
    response={
        200: None,
        422: FormInvalidResponseContract,
        401: MsgResponseContract,
    },
)
def authlogin(request: HttpRequest, response: HttpResponse, data: LoginFormContract):
    form = AuthenticationForm(data=data.dict())
    if form.is_valid() is False:
        return 422, {"errors": form.errors.get_json_data(escape_html=True)}

    user = authenticate(
        username=form.cleaned_data.get("username"),
        password=form.cleaned_data.get("password"),
    )
    if user is not None:
        login(request, user)  # returns a 200
    else:
        return 401, {"message": "Login refused"}


@router.get(
    "/logout",
    response={200: None, 403: None},
)
def authlogout(request: HttpRequest):
    if request.user.is_anonymous is True:
        return 403
    logout(request)  # returns a 200


@router.get("/state", auth=None, response={200: StateContract})
def global_state(request: HttpRequest):
    out = {"is_connected": False, "username": "anonymous"}
    if request.user.is_anonymous is False:
        out["is_connected"] = True
        out["username"] = request.user.get_username()
    # set a csrf token cookie
    get_token(request)
    return 200, out
