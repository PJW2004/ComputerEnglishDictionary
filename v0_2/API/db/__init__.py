if __name__ == "__main__": # absolute path
    from API.db.database import engine

    # Table create 아니 포트를 바꾸어도 이렇게 안되네 씁
    conn = engine.connect()
    # with engine.connect as conn:
    #     meta.create_all(conn, checkfirst=False)

