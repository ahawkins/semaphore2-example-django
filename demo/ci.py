from .settings import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'USER': 'postgres',
    'NAME': 'postgres',
    'HOST': 'localhost'
}
