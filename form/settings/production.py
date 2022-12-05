from .base import *

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["scholarshipform.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://scholarshipform.up.railway.app"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER':os.environ.get('PGUSER'),
        'PASSWORD':os.environ.get('PGPASSWORD'),
        'HOST':os.environ.get('PGHOST'),
        'PORT':os.environ.get('PGPORT')

}
}
