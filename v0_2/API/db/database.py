from db_secret_data import DB_user
from db_secret_data import DB_passwd
from db_secret_data import DB_host
from db_secret_data import DB_port
from db_secret_data import DB_name
print('env setting')

from sqlalchemy import create_engine
print('create engine')
from sqlalchemy.ext.declarative import declarative_base
print('declarative_base')
from sqlalchemy.orm import sessionmaker
print('sessionmaker')

url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
print(url)
engine = create_engine(url)
print(engine)
SessionLocal = sessionmaker(bind=engine)
print(SessionLocal)
Base = declarative_base
print(Base)
