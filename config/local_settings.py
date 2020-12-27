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