from API.db.db_secret_data import DB_user
from API.db.db_secret_data import DB_host
from API.db.db_secret_data import DB_port
from API.db.db_secret_data import DB_name
from API.db.db_secret_data import DB_passwd

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = f"postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}"
engine = create_engine(url)
SessionLocal = sessionmaker(engine)

Base = declarative_base