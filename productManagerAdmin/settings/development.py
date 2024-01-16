from .settings import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kx9(#^w26&3ke2vv74+ce)3@jmo5(hd3sj8$bu@=c=s0qk17dy'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = [
    "28995a08-967c-4174-a338-4045d3a51647-00-172c7oul7vayl.worf.replit.dev"
]

CSRF_TRUSTED_ORIGINS = [
    "https://28995a08-967c-4174-a338-4045d3a51647-00-172c7oul7vayl.worf.replit.dev"
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
