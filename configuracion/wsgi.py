import os
from decouple import config
from django.core.wsgi import get_wsgi_application

"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings') # este apunta al setings viejo no al folder
application = get_wsgi_application()
"""


#Necesitamos que django detecte automaticamente el entorno donde se encuentra sea desarrollo/produccion o local/render

# Detectar entorno
if config('RENDER_EXTERNAL_HOSTNAME', default=None):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings.produccion')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings.local')

application = get_wsgi_application()