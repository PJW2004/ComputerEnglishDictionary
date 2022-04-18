import sqlalchemy.exc

from API.db.database import engine

from translate import get_translate


conn = engine.connect()


def in_word(data_=None):
    insert = f"INSERT INTO userdata VALUES('{data_['단어']}', '{data_['해석']}')"

    try:
        conn.execute(insert)
        print('[정상적으로 입력되었습니다.]')

    except sqlalchemy.exc.IntegrityError:
        print('[이미 존재하는 단어 입니다.]')
        user_ = input('[다른 단어로 입력하시겠습니까?][Y/N] : ')
        if user_ == 'Y':
            return running()
        else:
            print('프로그램을 종료합니다.\n')

# test

def running():
    user = input('\n[입력할 용어를 적어 주세요]\n[한 👉 영] : ')
    data = {"단어": user,
            "해석": get_translate(user)}
    YN = input(f'\n[data가 최종적으로 {data} 처럼 저장이 됩니다.]\n[변경하지 않겠습니까? (Y/N)] : ')

    if YN == 'N':
        data["해석"] = input('[변경될 영어 번역을 입력해 주세요] : ')
        in_word(data_=data)

        print(conn.execute('select * from userdata'))

    else:
        print(data)
        in_word(data_=data)

        for i in conn.execute('select * from userdata'):
            print(i)


running()
