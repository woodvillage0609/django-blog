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

# AWS_ACCESS_KEY_ID = 'AKIAR64PX34I7ZDUFIWW'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'django-synctown'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}

# AWS_LOCATION = 'media'
# MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = 'public-read'