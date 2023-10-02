import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL_PREFIX = os.environ.get('DB_URL_PREFIX')
DATABASE_HOST = os.environ.get('DB_HOST')
DATABASE_USER = os.environ.get('DB_USER')
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')
DATABASE_PORT = os.environ.get('DB_PORT')
DATABASE_NAME = os.environ.get('MYSQL_DATABASE')
DATABASE_URL = f"{DATABASE_URL_PREFIX}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
