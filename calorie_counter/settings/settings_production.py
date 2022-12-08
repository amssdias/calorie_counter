from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS", "*")]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", "initial_database"),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", ""),
        "PORT": os.environ.get("DB_PORT", ""),
    }
}

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
