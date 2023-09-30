import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = database_url = os.environ.get('DB_URL')
