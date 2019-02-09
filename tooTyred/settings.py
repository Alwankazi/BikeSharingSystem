"""
Django settings for tooTyred project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&wu^h*s^#5(*1i3ab=cbo&*6+f+qph3s5(peuc-7&g79h*cqc('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tootyred.com','127.0.0.1','toootyred.pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'bootstrap3',
    'optrApp',
    'manApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tooTyred.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'tooTyred.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
WSGI_APPLICATION = 'tooTyred.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tootyred',
        'USER':'root',
        'PASSWORD':'tootyred',#superusertootyred
        'HOST':'localhost',#toootyred.mysql.pythonanywhere-services.com
        'PORT':''
    }
}

##PYTHON pythonanywhere


#DATABASES = {
##    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'toootyred$tootyred',
#        'USER':'toootyred',
#        'PASSWORD':'superusertootyred',#superusertootyred
#        'HOST':'toootyred.mysql.pythonanywhere-services.com',#toootyred.mysql.pythonanywhere-services.com
#        'PORT':''
#    }
#}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT ='/home/toootyred/TooTyred'

LOGIN_REDIRECT_URL='/login_success/'
LOGIN_REDIRECT_EMP_URL='/operator/log/'
LOGIN_REDIRECT_MAN_URL='/manager/log/'
LOGOUT_REDIRECT_URL='/home/'

LOGIN_URL = '/home/login/'
LOGIN_EXEMPT_URL = (
    r'^home/logout$',
    r'^home/register/$',
    r'^home/$',
    r'^home/reset-password/$',
    r'^home/reset-password/done/$',
    r'^home/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
    r'^home/reset-password/complete/$',
    r'^home/termsandconditions/$',
    r'^operator/$',
    r'^manager/$',
    r'^employee/$',
)

LOGIN_EXEMPT_EMPLOYEE_URL = (
    r'^home/reservations/$',
    r'^home/reserve/$',
    r'^home/account/$',
    r'^home/changeaccount/$',
    r'^home/deleteaccount/$',
    r'^home/changepassword/$',
    #managers pages come here
)

LOGIN_EXEMPT_USER_URL = (
    r'^operator/log/$',
    r'^operator/bikes/$',
    r'^operator/station[0-9]/$',
    r'^operator/customerservice/$',
    #managers pages come here
)

LOGIN_EXEMPT_MANAGER_URL = (
    r'^manager/log/$',
    r'^manager/usagereports/$',
    r'^manager/statistics/$',
    r'^manager/dailyreports/$',
    #employee and users come here
)
#password tootyred12345
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tootyred.com@gmail.com'
EMAIL_HOST_PASSWORD = 'samwqdqbutvkyisp'
EMAIL_PORT = 587
