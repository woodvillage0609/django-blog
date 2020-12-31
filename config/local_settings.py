import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'yx2szqin)a0jo72t=y&e_sf9vyfh%*asz^#gnx5rh0(2$gebzk'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'blog_django',
        # 'USER': 'root',
        # 'PASSWORD': 'Iymy1800@',
        # 'HOST': '',
        # "PORT": '',
    }
}

DEBUG = True

#画像表示のpillow関連。投稿した写真が保存される場所を指定
#settings.pyからこちらに移行。ローカル環境では、mediaフォルダ、本番環境ではS3に保存とするため。
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'