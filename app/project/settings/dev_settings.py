from ._base import *


DEBUG = True


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/frontend/dist/')
]

