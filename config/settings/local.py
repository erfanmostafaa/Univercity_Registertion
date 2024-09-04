from .base import *  # noqa
from .base import env
import environ
# GENERAL

# env files
django_env = environ.Env()
django_env.read_env(str(BASE_DIR / ".envs/.local/.django"))
database_env = environ.Env()
database_env.read_env(str(BASE_DIR / ".envs/.local/.postgres"))
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
# local databases
DATABASES = {
    'default': {
        'ENGINE': database_env('MAIN_DB_ENGINE'),
        'NAME': database_env('MAIN_DB_NAME'),
        'USER': database_env('MAIN_DB_USER'),
        'PASSWORD': database_env('MAIN_DB_PASSWORD'),
        'HOST': database_env('MAIN_DB_HOST'),
        'PORT': database_env('MAIN_DB_PORT'),
    }
}

DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = django_env(
    "DJANGO_SECRET_KEY",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = django_env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
# INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
# INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# Your stuff...
# ------------------------------------------------------------------------------
