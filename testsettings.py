from os.path import dirname, join

SECRET_KEY='abcde12345'

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS=(
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'recursive_postgres'
)

SITE_ID=1

TEST_ROOT=join(dirname(__file__), 'tests')

MIDDLEWARE_CLASSES=()
