from API.db.database import engine


from API.user import user_pass_li

conn = engine.connect()


user = input('[삭제할 대상을 입력해 주세요][user/word] : ')
if user == 'user':
    user_li, passwd_li = user_pass_li()
    print(user_li, passwd_li)
    user_data = input("[삭제할 계정 이름을 입력해 주세요.] : ")
    passwd = input("[passwd] : ")
    try:
        if user_data == user_li[passwd_li.index(passwd)]:
            delete = f"DELETE FROM userlist WHERE users_='{user_data}'"

            conn.execute(delete)
        else:
            print('존재하지 않는 계정입니다.')
    except ValueError:
        print('존재하지 않는 비번입니다.')
