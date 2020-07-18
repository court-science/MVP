from .base import *

DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True

SECURE_REFERRER_POLICY = "strict-origin"

SECURE_BROWSER_XSS_FILTER = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_zo10w!04#yw*-ye&bh=g8pk0w=n20sp1lxm4mdpvdk)m3!h!-'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbhrbrht580khr',
        'USER': 'ydibqwvgxgyzym',
        'PASSWORD': '754c456a7ce1d572dc5b7dabf69f5ceabf0f5a9326c912ae2440a6db7f8133ce',
        'HOST': 'ec2-34-197-141-7.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
