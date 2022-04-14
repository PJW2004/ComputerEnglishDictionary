import os
from dotenv import load_dotenv

load_dotenv()

DB_user = os.environ.get('TEST_USER')
DB_passwd = os.environ.get('TEST_PASSWD')
DB_host = os.environ.get('TEST_IP')
DB_port = os.environ.get('TEST_PORT')
DB_name = os.environ.get('TEST_DBNAME')