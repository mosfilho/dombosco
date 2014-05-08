# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

urlpatterns = []

def configure(**extra):
    from django.conf import settings
    os.environ['DJANGO_SETTINGS_MODULE'] = 'filer.test_utils.cli'
    defaults = dict(
        DEBUG=True,
        TEMPLATE_DEBUG=True,
        DATABASE_SUPPORTS_TRANSACTIONS=True,
        DATABASES={
            'default': {'ENGINE': 'django.db.backends.sqlite3'}
        },
        USE_I18N=True,
        MEDIA_ROOT='/media/',
        STATIC_ROOT='/static/',
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        SECRET_KEY='key',
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
            ),
        INSTALLED_APPS = [
            'filer',
            'mptt',
            'easy_thumbnails',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.staticfiles',
            ],
        ROOT_URLCONF='filer.test_utils.cli',
    )
    defaults.update(extra)
    settings.configure(**defaults)
    from django.contrib import admin
    admin.autodiscover()
