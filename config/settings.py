"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

#Heroku向けに追加
#import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yx2szqin)a0jo72t=y&e_sf9vyfh%*asz^#gnx5rh0(2$gebzk'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#Herokuデプロイのため、色々変更を加えています。 
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEBUG = False


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #own
    'blogs',
    'citymaps',
    'crispy_forms',
    'account',
    'bootstrap4',
    'ckeditor',
    'ckeditor_uploader'
]

#CKeditorに投稿する写真とかのパス
CKEDITOR_UPLOAD_PATH = "uploads/"
#CKeditorのカスタマイズ関連
CKEDITOR_CONFIGS = {
    'default': {
        'height': 600,
        'width': '100%',
        'toolbar': 'full',
        'extraPlugins': 'codesnippet, widget, lineutils',
        'codeSnippet_theme':'monokai',
    },
}

GOOGLE_MAPS_API_KEY = 'AIzaSyBTc38KnsEtHKwTSOB28FsLEdi156ogLmk'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Herokuのため追加
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'django.template.context_processors.media', #画像用投稿向けに追加
                'blogs.context.related', #blogのrelation関係
            ],
            #bootstrap4使用のため
            'builtins':[ 
               'bootstrap4.templatetags.bootstrap4',
           ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#local_settings.pyの方に移行。
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'blog_django',
        #'USER': 'root',
        #'PASSWORD': 'Iymy1800@',
    #}
#}


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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#加えてあげた。Herokuデプロイのため。
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

#別途作成したstaticフォルダ（css, java, img)に集約させるための表記
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#画像表示のpillow関連。投稿した写真が保存される場所を指定
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#Crispy_formをインストールした際に行った設定
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#ログイン時にDjangoでは自動的にprofileに飛ぶので、homeとしてあげる。
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

#Heroku向けに追加。一番下に持ってこないとワークしない。。らしいが。
try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
