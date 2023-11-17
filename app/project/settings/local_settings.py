import os

from dotenv import load

from .dev_settings import *


load()

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SECRET_KEY = 'django-insecure-%xpml87sca6a#ja3sqa#1#la^u#h!^4r9rv2i*+a1#8&3#+y&9'