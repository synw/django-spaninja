# from unittest.mock import Mock
import jwt

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string


def email_message(message, subject, to_email):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])


def email_activation_token(request, user, to_email, subject, template):
    current_site = get_current_site(request)
    domain = current_site.domain
    token = jwt.encode({"email": user.email}, settings.SECRET_KEY, algorithm="HS256")
    message = render_to_string(
        template,
        {"domain": domain, "token": token},
    )
    email_message(message, subject, to_email)
