# flake8: noqa
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

import socket

import os

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['*']

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='m6g#m5uy&4^!ji!*4z4cnh*56yhwjz*t5m35)+!dn7^ljqc2zc')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SMTP_HOST = 'smtp.zoho.com'
DEFAULT_EMAIL = 'nzaniela@nzaniela.com'
DEFAULT_EMAIL_PASSWORD = 'sepham89'

EMAIL_HOST = SMTP_HOST
EMAIL_HOST_USER = DEFAULT_EMAIL
EMAIL_HOST_PASSWORD = DEFAULT_EMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
#                     default='django.core.mail.backends.console.EmailBackend')

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1"]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions',)

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
