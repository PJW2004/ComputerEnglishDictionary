from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geturl import yaml_loader


url = yaml_loader("config.yaml")
engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base = declarative_base
