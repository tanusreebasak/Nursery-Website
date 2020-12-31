import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

