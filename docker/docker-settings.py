DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://10.5.0.1:8005'

APIS = {
    'authentication': 'http://10.5.0.1:8005',
    'base': 'http://10.5.0.1:8005',
    'booth': 'http://10.5.0.1:8005',
    'census': 'http://10.5.0.1:8005',
    'mixnet': 'http://10.5.0.1:8005',
    'postproc': 'http://10.5.0.1:8005',
    'store': 'http://10.5.0.1:8005',
    'visualizer': 'http://10.5.0.1:8005',
    'voting': 'http://10.5.0.1:8005',
}
