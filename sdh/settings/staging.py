# from .base import *

print('secret_key before:', SECRET_KEY)
django_heroku.settings(locals())
print('secret_key after:', SECRET_KEY)
