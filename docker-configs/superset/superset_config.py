import os

from werkzeug.contrib.cache import RedisCache

### Getting Environment Variables
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'superset_postgres') #set w/ hostname
POSTGRES_DB = os.getenv('POSTGRES_DB', '')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_USER = os.getenv('POSTGRES_USER', '')
REDIS_HOST = os.getenv('REDIS_HOST', 'superset_redis') #set w/ hostname
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'thisISaSECRET_1234')

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': int(REDIS_PORT),
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://' + REDIS_HOST + ':'+ REDIS_PORT + '/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@' + POSTGRES_HOST + ':'+ POSTGRES_PORT +'/'+POSTGRES_DB
SQLALCHEMY_TRACK_MODIFICATIONS = True


class CeleryConfig(object):
    BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=int(REDIS_PORT),
    key_prefix='superset_results'
)
