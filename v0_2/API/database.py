from db_secret_data import DB_user
from db_secret_data import DB_passwd
from db_secret_data import DB_host
from db_secret_data import DB_port
from db_secret_data import DB_name

from sqlalchemy import create_engine

# psycopg 에러와 같은 경우 rosetta ERROR 때문에 사용 못함
# -> window에서 사용가능
url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
engine = create_engine(url)
