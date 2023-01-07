import json

from django.contrib.admin.views.decorators import staff_member_required

from ninja import NinjaAPI
from ninja.security import django_auth
from ninja.errors import ValidationError

from backend.apps.account.api import router as account_router


api_kwargs = {
    "auth": django_auth,
    "csrf": True,
    "docs_decorator": staff_member_required,
}
api = NinjaAPI(**api_kwargs)


@api.exception_handler(ValidationError)
def custom_validation_errors(request, exc):
    print(json.dumps(exc.errors, indent=2))
    return api.create_response(request, {"detail": exc.errors}, status=418)


api.add_router("/account/", account_router)
