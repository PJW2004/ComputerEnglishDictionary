from db_secret_data import DB_user
from db_secret_data import DB_passwd
from db_secret_data import DB_host
from db_secret_data import DB_port
from db_secret_data import DB_name
print('env setting')


from sqlalchemy import create_engine

url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
engine = create_engine(url)
