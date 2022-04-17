# user
import sqlalchemy.exc

from API.db.database import engine, Base
from API.db import models

Base.metadata.create_all(engine)

print('[로그인을 먼저 해주셔야 프로그램이 시작됩니다.] : 계정이 없다면 "회원가입"을 입력해주세요')
conn = engine.connect()


def user_login():
    print('[로그인]')
    user = input('user : ')
    return user


def create_user():
    user = input('[회원가입할 username을 입력해주세요][영어만 지원이 됩니다.] : ')
    passwd = input('[user의 비번은?] : ')
    insert = f"INSERT INTO userlist VALUES('{user}', '{passwd}')"

    conn.execute(insert)


def running_cre_u():
    try:
        create_user()

        print("[정상적으로 만들어 졌습니다.]\n")

    except sqlalchemy.exc.IntegrityError:
        print('[이미 존재하는 계정 이름입니다.]\n')
        create_user()

        
def running(user_="", user_li=None):
    if user_ == '회원가입':

    elif user_ in user_li:
        print(user_)
    else:
        YN = input('[계정이 존재 하지 않습니다. 계정을 만드시겠습니까?][Y/N] : ')


ins = "select users_ from userlist"

result = conn.execute(ins)
user_li = []
for i in result:
    user_li.append(i[0])

print(user_li)

user = user_login()

running(user_=user, user_li=user_li)


