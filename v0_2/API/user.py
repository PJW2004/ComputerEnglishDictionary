# user
import sqlalchemy.exc

from API.db.database import engine, Base
from API.db import models

Base.metadata.create_all(engine)

print('[로그인을 먼저 해주셔야 프로그램이 시작됩니다.] : 계정이 없다면 "회원가입"을 입력해주세요')
user = input('user : ')
conn = engine.connect()


def create_user():
    user = input('[회원가입할 username을 입력해주세요][영어만 지원이 됩니다.] : ')
    passwd = input('[user의 비번은?] : ')
    insert = f"INSERT INTO userlist VALUES('{user}', '{passwd}')"
    print(insert)
    conn.execute(insert)


if user == '회원가입':
    try:
        create_user()
    except sqlalchemy.exc.IntegrityError:
        print('[이미 존재하는 계정 이름입니다.]')
        create_user()

else:
    pass
