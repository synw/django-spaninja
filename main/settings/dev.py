from os import path
from .settings import BASE_DIR
from . import exec_file

EMAIL_FILE_PATH = BASE_DIR / "email"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

exec_file(path.join(BASE_DIR, "localsettings.py"), locals(), globals())
