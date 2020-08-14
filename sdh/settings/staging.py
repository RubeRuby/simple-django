from .base import *

print('secret_key before:', SECRET_KEY)
django_heroku.settings(locals(), secret_key=False)
print('secret_key after:', SECRET_KEY)
