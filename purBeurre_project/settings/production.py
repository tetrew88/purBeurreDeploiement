from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'
DEBUG = False
ALLOWED_HOSTS = ['185.98.139.132']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'purBeurre', # le nom de notre base de données créée précédemment
        'USER': 'tetrew', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'Doni88650',
        'HOST': '',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = ['authentification.views.EmailBackend']
