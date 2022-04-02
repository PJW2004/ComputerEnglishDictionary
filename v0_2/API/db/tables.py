from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy import MetaData

from database import Base, engine

'''
create table list
1. userdata
2. user_list
'''

# metadata
meta = MetaData()

userdata = Table(
    'userdata', meta,
    Column('word', String, primary_key=True),
    Column('meaning', String, unique=False),
    # foreign Key
    Column('user', String, ForeignKey("user_list.user"), unique=False)
)

User_list = Table(
    'user_list', meta,
    Column('user', String, primary_key=True),
    Column('passwd', String, unique=False)
)

# Table create
with engine.connect as conn:
    meta.create_all(conn, checkfirst=False)
    

