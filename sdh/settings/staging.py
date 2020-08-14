from .base import *

print('secret_key before:', SECRET_KEY)
django_heroku.settings(secret_key=False, locals())
print('secret_key after:', SECRET_KEY)
