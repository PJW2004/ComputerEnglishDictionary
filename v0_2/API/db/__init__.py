from API.db.database import engine
import models

if __name__ == "__main__": # absolute path
    # Table create 아니 포트를 바꾸어도 이렇게 안되네 씁
    conn = engine.connect()


