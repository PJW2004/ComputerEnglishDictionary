import os
from dotenv import load_dotenv

load_dotenv()

DB_user = os.environ.get('DB_USER')
DB_passwd = os.environ.get('DB_PASSWD')
print(DB_user)
print(DB_passwd)
