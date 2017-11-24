"""
Django settings for wechat project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging
import django.utils.log
import logging.handlers
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=l#p3i_5whz)tjldphd4+=-k8vo9d#w3gro5%w*xfs6e8e3j^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','59.110.4.24','www.gongzuofuwu.com','gongzuofuwu.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oa',
    'gift',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oa.middleware.SimpleMiddleware',
    'gift.middleware.SimpleMiddleware'
]

ROOT_URLCONF = 'wechat.urls'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# SESSION_COOKIE_NAME ＝ 'sessionid'
# Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"              # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None             # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False          # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True         # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 60*30             # Session的cookie失效日期（半小时）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False        # 是否每次请求都保存Session，默认修改之后才保存（默认）



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

WSGI_APPLICATION = 'wechat.wsgi.application'


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', #数据库引擎
            'NAME': 'oa',                         #数据库名
            'USER': 'root',                       #用户名
            'PASSWORD': 'root',                   #密码
            'HOST': '',                           #数据库主机，默认为localhost
            'PORT': '',                           #数据库端口，MySQL默认为3306
            'OPTIONS': {
                'autocommit': True,
            },
        }
}




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "wechat/common_static")
    # os.path.join("", "/oa/MP_verify_sg9VcvfPWosULKNp.txt")
]





LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'default': {  # 默认
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/all.log',  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {  # 错误
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/error.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {  # 控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'request_handler': {  # request请求
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {  # script请求
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'wechat.views': {
            'handlers': ['default', 'error','console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

