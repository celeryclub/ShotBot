import os
import sys

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Michael Meyer', 'mikemeyer@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE':	 'django.db.backends.postgresql_psycopg2',
		'NAME':		   'looklab',
		'USER':		   'looklab',
		'PASSWORD': 'looklab',
		'HOST':		   '',
		'PORT':		   '',
	}
}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

TWITTER_CONSUMER_KEY = 'PYfLfTVFYEHkttJi3jBg'
TWITTER_CONSUMER_SECRET = 'xWG0usnrMDah17gzE578ZkUH0ZdZyJF9fefwFQBpPq0'
TWITTER_REQUEST_TOKEN_URL 'http://twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'http://twitter.com/oauth/access_token'
TWITTER_AUTH_URL = 'http://twitter.com/oauth/authorize'

sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '%6*pc8c#v44l!#l^@!meomm1i!pjy0fm%1bh%0vir3z-lodmh2'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'shotbot.urls'

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates"),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}
