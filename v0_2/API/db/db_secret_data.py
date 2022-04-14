import os
from dotenv import load_dotenv

load_dotenv()

# DB_user = os.environ.get('DB_USER')
# DB_passwd = os.environ.get('DB_PASSWD')
# DB_host = os.environ.get('DB_IP')
# DB_port = os.environ.get('DB_PORT')
# DB_name = os.environ.get('DBNAME')

DB_user = os.environ.get('TEST_USER')
DB_passwd = os.environ.get('TEST_PASSWD')
DB_host = os.environ.get('DB_IP')
DB_port = os.environ.get('TEST_PORT')
DB_name = os.environ.get('TEST_DBNAME')
