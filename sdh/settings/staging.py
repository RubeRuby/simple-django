from .base import *

SECRET_KEY = 'some-key'
print('secret_key before:', SECRET_KEY)
django_heroku.settings(locals(), secret_key=False)
print('secret_key after:', SECRET_KEY)
