"""
Django settings for sims_project project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the following line in .env, .bashrc, .bash_profile or .zshrc where Shell read its contents when loading: 
# this is the real key to be hidden from the public 
#      export  DJANGO_SECRET_KEY='aq*insto=jr436h=m7&fp(j@(v!sz1tq&97s6kn51ha&jy(_8(')   ### << get a new one by creating a new django project
#      export  DJANGO_DEBUG=""
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '8#0q@*y)8-69kxan2jci5d(mb0f&o11-6(rm&y4rrvpg-63@0c')
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['sngreecu.pythonanywhere.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sims101', 
    'crispy_forms', 
    'commons', 
    'xlwt', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'sims_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), 
        ],
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

WSGI_APPLICATION = 'sims_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization  -- dj2ExCh9
# https://docs.djangoproject.com/en/2.2/topics/i18n/

from django.utils.translation import gettext_lazy as _ 
LANGUAGE_CODE = 'en'       #'en-us'   
# LANGUAGE_CODE = 'es-EC'
LANGUAGES = [
    ('en', _('English')), 
    ('es', _('Spanish')), 
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'), 
)

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True


LOGIN_REDIRECT_URL = 'home'    # place to go after login  if no "next" parameter is present in the request (GET parameter)
LOGIN_URL = 'login'            # The URL to redirect the user to log in 
LOGOUT_URL = 'logout'          # The URL to redirect the user to log out

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'




