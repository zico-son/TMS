from .common import *

SECRET_KEY = 'django-insecure-ki2j_&zb!dq%0d90ezdj^b(b57qsmpp40+oomc97dxo+4s63l-'

ALLOWED_HOSTS = ['web-production-c1b7.up.railway.app']
DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'afaker',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'Ahmed@123',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-c1b7.up.railway.app'
]