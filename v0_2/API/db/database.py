from db_secret_data import DB_user
from db_secret_data import DB_passwd
from db_secret_data import DB_host
from db_secret_data import DB_port
from db_secret_data import DB_name
print('env setting')

# url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = f"postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
