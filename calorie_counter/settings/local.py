SECRET_KEY="django-insecure-+01rjt^m#w9_jxu!s6##q3j6fch*i5_h#_x4rn0q!zni&3qmls"

DEBUG = True

# Celery
CELERY_ENABLED = False

# HTTPS
SESSION_COOKIE_SECURE = False
SECURE_SSL_HOST = ""
SECURE_SSL_REDIRECT = False

# LOGS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {
        "django": {
            "handlers": ["file_info", "file_warning", "file_error"],
            "level": "INFO",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple_format",
        },
        "file_info": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/info.log",
            "formatter": "simple_format",
        },
        "file_warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "./logs/warning.log",
            "formatter": "warning_format",
        },
        "file_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "./logs/error.log",
            "formatter": "error_format",
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