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
    'userdata', meta
    
)