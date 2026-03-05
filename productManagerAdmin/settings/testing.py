from .settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-w%+3)e91q)&k%1tm457x4@jdae1q3ln9@r%m--#iz9x%uxkgf+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Você também pode deixar em branco com colchetes vazios []
ALLOWED_HOSTS = ["127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
