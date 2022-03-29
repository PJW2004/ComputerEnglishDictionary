import os
from dotenv import load_dotenv


load_dotenv()

DB_user = os.environ.get('DB_USER')
print(DB_user)
