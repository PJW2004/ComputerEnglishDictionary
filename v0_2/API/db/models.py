from .database import Base
from sqlalchemy import Column, String, ForeignKey

class userdata(Base):
    __tablename__ == 'userdata'

    Column('word', String, primary_key=True),
    Column('meaning', String, unique=False),
    # foreign Key
    Column('user', String, ForeignKey("user_list.user"), unique=False)