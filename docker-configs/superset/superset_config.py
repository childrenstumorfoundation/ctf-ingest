import os

from werkzeug.contrib.cache import RedisCache

### Getting Environment Variables
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'superset_postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', '')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_USER = os.getenv('POSTGRES_USER', '')
REDIS_HOST = os.getenv('REDIS_HOST', 'superset_redis')

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'superset_redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://' + REDIS_HOST + ':6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://superset:superset@superset_postgres:5432/superset'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'


class CeleryConfig(object):
    BROKER_URL = 'redis://superset_redis:6379/0'
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'redis://superset_redis:6379/0'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host='superset_redis',
    port=6379,
    key_prefix='superset_results'
)
