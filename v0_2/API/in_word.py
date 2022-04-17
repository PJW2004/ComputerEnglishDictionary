from API.db.database import engine

from translate import get_translate


user = input('[입력할 용어를 적어 주세요]\n[한 👉 영] : ')
data = {"단어": user,
        "해석": get_translate(user)}
YN = input(f'\n[data가 최종적으로 {data} 처럼 저장이 됩니다.]\n[변경하지 않겠습니까? (Y/N)] : ')
conn = engine.connect()


def in_word(data_=None):
    insert = f"INSERT INTO userdata VALUES('{data_['단어']}', '{data_['해석']}')"

    conn.execute(insert)
    print('[정상적으로 입력되었습니다.]')


if YN == 'N':
    data["해석"] = input('[변경될 영어 번역을 입력해 주세요] : ')
    print(data)
    in_word(data_=data)


else:
    print(data)
    in_word(data_=data)
