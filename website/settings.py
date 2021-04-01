#-*- coding: utf-8 -*-
"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from website import utils

import ldap
from django_auth_ldap.config import LDAPSearch,ActiveDirectoryGroupType

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l6!iqe*&w2^r^!bcq=7g2@6c)izv+chj$+!tw+yyn+fqd5#dzk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'cmdb.apps.CmdbConfig',
    'publisher.apps.PublisherConfig',
    'returner.apps.ReturnerConfig',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'website.tokenAuth.ExpiringTokenAuthentication',
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : utils.MYSQL_DB,
        'USER' : utils.MYSQL_USER,
        'PASSWORD' : utils.MYSQL_PASS,
        'HOST' : utils.MYSQL_HOST,
        'PORT' : utils.MYSQL_PORT,
    }
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend', 
    'django.contrib.auth.backends.ModelBackend',
) 

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# TEMPLATE zh_CN
FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

# ldap auth
AUTH_LDAP_SERVER_URI = 'ldap://'+utils.LDAP_URL+':'+utils.LDAP_PORT
AUTH_LDAP_BIND_DN = utils.LDAP_BIND
AUTH_LDAP_BIND_PASSWORD = utils.LDAP_PWD
OU = utils.LDAP_OU
AUTH_LDAP_USER_SEARCH = LDAPSearch(OU, ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {  
    "first_name": "givenName",
    "last_name": "cn",
    "username": "givenName",
}

AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(OU,ldap.SCOPE_SUBTREE, "(objectClass=group)" )


AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300
AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: False,
    ldap.OPT_REFERRALS: False,
}

AUTH_LDAP_FIND_GROUP_PERMS = True


#ldaplog
import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)