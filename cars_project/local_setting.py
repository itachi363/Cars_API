# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5m3sinbw5df$4s5ufnpram9r%hneofl^s8pet$&n(tt7z201q4'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}