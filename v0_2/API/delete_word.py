from .db.database import engine

conn = engine.coonnect()


user = input('[삭제할 대상을 입력해 주세요][user/word] : ')
if user == 'user':
    data = input("[삭제할 계정 이름을 입력해 주세요.]")
    delete = f'DELETE FROM userlist WHERE users_="{data}"'
    