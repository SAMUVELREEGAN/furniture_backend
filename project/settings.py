from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-an1zlpr%*mnyzjmrqxg_+l(up7ckxmq2jxsy-orkbp*%^_flqe'

DEBUG = True

ALLOWED_HOSTS = ['furniture-backend-y7hu.onrender.com' , 'localhost' , '127.0.0.1']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'Pro_banner',
    'Logo',
    'categories',  
    'colorList', 
    'type',
    'weblink',
    'proSize',
    'product',
    'craft',
    'enquirie',
    'carosel',
    'app',
    'contactinfo',
    'book',
    'reviews'
]

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'samuelreegan372@gmail.com'
EMAIL_HOST_PASSWORD = 'uvrosezsejqaajco'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CONTACT_RECEIVER_EMAIL = 'samuelreegan372@gmail.com'

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'postgresql://veera_user:GaPWGvcjs2sMapAz6bHR01d3SUDZfnaB@dpg-d0o5gm6mcj7s73e5d64g-a/veera_ragav'),  # This will read from Render environment variable
        conn_max_age=600,
        ssl_require=True
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # ✅ REQUIRED for collectstatic
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_URL = 'http://localhost:8000'
