from .database import Base
from sqlalchemy import Column, String, ForeignKey


class userdata(Base):
    __tablename__ = 'userdata'

    word = Column('word', String, primary_key=True)
    meaning = Column('meaning', String, unique=False)
    # foreign Key
    user = Column('user', String, ForeignKey("user_list.user"), unique=False)

class userlist(Base):
    __tablename__ = 'userlist'

    user = Column('user', String, primary_key=True)
    passwd = Column('passwd', String, unique=False)
