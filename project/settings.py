from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-an1zlpr%*mnyzjmrqxg_+l(up7ckxmq2jxsy-orkbp*%^_flqe'

DEBUG = True

ALLOWED_HOSTS = []



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

CORS_ALLOWED_ORIGINS=["http://localhost:3000"]

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

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'samuelreegan372@gmail.com'         
EMAIL_HOST_PASSWORD = 'uvrosezsejqaajco' 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CONTACT_RECEIVER_EMAIL = 'samuelreegan372@gmail.com'


WSGI_APPLICATION = 'project.wsgi.application'

LOGIN_REDIRECT_URL = '/admin/'



DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'veera_ragav',
        'USER':'root',
        'PASSWORD':'ree007@mas',
        'HOST':'localhost',
        'PORT':3306
    }

}





LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
MEDIA_URL = '/media/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')


SITE_URL = 'http://localhost:8000'
