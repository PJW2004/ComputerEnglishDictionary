import os

from API.db.database import engine

try:
    conn = engine.connect()


    user = input('[삭제할 대상을 입력해 주세요][user/word] : ')
    if user == 'user':
        ins = "select * from userlist"

        result = conn.execute(ins)
        user_li = []
        passwd_li = []
        for i in result:
            user_li.append(i[0])
            passwd_li.append(i[1])

        print(user_li, passwd_li)
        user_data = input("[삭제할 계정 이름을 입력해 주세요.] : ")
        passwd = input("[passwd] : ")
        try:
            if user_data == user_li[passwd_li.index(passwd)]:
                delete = f"DELETE FROM userlist WHERE users_='{user_data}'"

                conn.execute(delete)
                print('삭제가 완료 되었습니다.')
            else:
                print('존재하지 않는 계정입니다.')
        except ValueError:
            print('존재하지 않는 비번입니다.')

    elif user == 'word':
        ins = "select * from userdata"

        result = conn.execute(ins)
        word_li = []
        meaning_li = []
        for i in result:
            word_li.append(i[0])
            meaning_li.append(i[1])

        print(word_li, meaning_li)
        user_data = input('[삭제할 단어를 입력해 주세요.] : ')
        try:
            TF = input(f'[현재 선택한 단어는 {user_data}->{meaning_li[word_li.index(user_data)]}입니다.]\n[정말 삭제 하시겠습니까?][Y/N] : ')
            if TF == 'Y':
                delete = f"DELETE FROM userdata WHERE word='{user_data}'"

                conn.execute(delete)
                print('삭제가 완료 되었습니다.')
            else:
                print('삭제를 종료합니다.')

        except ValueError:
            print('존재하지 않는 단어 입니다.')
finally:
    os.system('python __init__.py')