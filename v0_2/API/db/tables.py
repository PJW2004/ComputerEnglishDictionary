from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData

from database import Base

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
    # 외래 Key
    Column('user', String, unique=False)
)

User_list = Table(
    'user_list', meta,
    Column('user', String, primary_key=True),
    Column('passwd', String, primary_key=True)
)