from API.db.database import engine
import models

if __name__ == "__main__": # absolute path
    # Table create 아니 포트를 바꾸어도 이렇게 안되네 씁
    # => 연결이 안된이유 : aws서버에서 inbound port를 안열어줌 ㅇㅇ
    conn = engine.connect()


