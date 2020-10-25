import os
from decouple import config

DB_HOST=config('DB_HOST')
DB_PORT=config('DB_PORT', cast=int)
DB_NAME=config('DB_NAME')
DB_USER=config('DB_USER')
DB_PASSWORD=config('DB_PASSWORD')

# CELERY_BROKER=<PLACEHOLDER>
# CELERY_BACKEND=<PLACEHOLDER>