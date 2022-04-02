import os

from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy import MetaData

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
try:
    from database import Base, engine, Session

    with engine.connect as conn:
        meta.create_all(conn, checkfirst=False)
except ImportError:
    os.system('pip3 uninstall psycopg2')
    os.system('pip3 install psycopg2-binary')
    # postgres APP 사용 경우
    # os.system('sudo ln -s /Applications/Postgres.app/Contents/Versions/9.4/lib/libpq.5.dylib /usr/lib')
