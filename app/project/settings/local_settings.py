import os

from dotenv import load_dotenv, find_dotenv

from .dev_settings import *

if DEBUG:
    load_dotenv(find_dotenv('.env.dev'))
else:
    load_dotenv(find_dotenv('.env.prod'))

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD')
    }
}


SECRET_KEY = os.environ.get('SECRET_KEY')
