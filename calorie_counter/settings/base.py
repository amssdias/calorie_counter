"""
Django settings for calorie_counter project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from dotenv import load_dotenv
from pathlib import Path
from django.urls import reverse_lazy

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS", "*")]

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_PROJECT_APPS = [
    'apps.accounts',
    'apps.foods',
]

INSTALLED_APPS = DJANGO_APPS + MY_PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'calorie_counter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calorie_counter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", ""),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('pt', 'Portuguese'),
    ('en', 'English'),
    ('es', 'Spanish'),
]

LOCALE_PATHS = [
    os.path.join(os.path.dirname(BASE_DIR), "apps/locale")
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = os.environ.get("STATIC_URL", '/static/')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')

# MEDIA FILES
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media/')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# AUTHENTICATION BACKENDS
AUTHENTICATION_BACKENDS = [
    'calorie_counter.backends.email_backend.EmailBackEnd',
    'django.contrib.auth.backends.ModelBackend',
]

# LOGIN SETTINGS
LOGIN_URL = reverse_lazy("accounts:login")
LOGOUT_REDIRECT_URL = reverse_lazy("accounts:login")

# CELERY SETTINGS
CELERY_ENABLED = True
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "redis://localhost"

# HTTPS
SESSION_COOKIE_SECURE = True
SECURE_SSL_HOST = ""
SECURE_SSL_REDIRECT = False


# LOGS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple_format",
        },
    },
    "formatters": {
        "simple_format": {
            "format": "{levelname:8s} {asctime}: {message} - {filename}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "warning_format": {
            "format": "{levelname:8s} {asctime}: {message} - {filename}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "error_format": {
            "format": "{levelname:8s}: {asctime} {filename} {message} - {pathname}: {lineno}",
            "style": "{",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    }
}

DJANGO_DEBUG_TOOLBAR = os.environ.get("DJANGO_DEBUG_TOOLBAR", True)
