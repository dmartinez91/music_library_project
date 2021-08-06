SECRET_KEY = 'django-insecure-xtr@jfg)ql3zx1kwdl%dg-3!5^3u$ja=ukrvj8)%0yrbj7eqxx'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'ollie3691',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}