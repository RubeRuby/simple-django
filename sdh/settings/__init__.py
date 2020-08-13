from .base import *

env_name = os.getenv('ENV_NAME', 'local')
print("env name: " + env_name)

if env_name == 'prod':
    from .production import *
elif env_name == 'dev':
    from .dev import *
else:
    from .local import *
