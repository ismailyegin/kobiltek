from oxiterp.settings.base import *

# Override base.py settings here


DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oxiterp',
        'USER': 'oxitowner',
        'PASSWORD': 'oxit2016',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


try:
    from oxiterp.settings.local import *
except :
    pass
