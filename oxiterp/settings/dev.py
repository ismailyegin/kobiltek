from oxiterp.settings.base import *

# Override base.py settings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oxiterp_wushu',
        'USER': 'postgres',
        'PASSWORD': 'oxit2016',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    from oxiterp.settings.local import *
except :
    pass
