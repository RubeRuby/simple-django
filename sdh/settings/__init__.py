from .base import *

env_name = os.getenv('ENV', 'local')
print("env name: " + env_name)

if env_name == 'PRODUCTION':
    from .production import *
elif env_name == 'STAGING':
    from .staging import *
else:
    from .local import *

