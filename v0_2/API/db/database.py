from API.db.db_secret_data import DB_user
from API.db.db_secret_data import DB_passwd
from API.db.db_secret_data import DB_host
from API.db.db_secret_data import DB_port
from API.db.db_secret_data import DB_name

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# psycopg 에러와 같은 경우 rosetta ERROR 때문에 사용 못함
# -> window에서 사용가능
url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
print(url)
engine = create_engine(url)
SessionLocal = sessionmaker(engine)

Base = declarative_base()
