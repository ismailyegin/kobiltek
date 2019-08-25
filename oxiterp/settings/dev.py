from oxiterp.settings.base import *

# Override base.py settings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sbswushu',
        'USER': 'postgres',
        'PASSWORD': 'kobil2013',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    from oxiterp.settings.local import *
except :
    pass
