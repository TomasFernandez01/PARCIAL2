from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración para servir archivos estáticos en desarrollo
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'