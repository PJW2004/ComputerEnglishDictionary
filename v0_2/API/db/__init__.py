if __name__ == "__main__": # absolute path
    # if __package__ is None:
    #     import sys
    #     from os import path
    #     print(path.dirname(path.dirname(path.abspath(__file__))))
    #     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    #     from API.db.database import engine
    # else:
    #     # database engine setting
    #     try:
    #         from API.db.database import engine
    #     # except ImportError:
    #     #     os.system('pip3 uninstall psycopg2')
    #     #     os.system('pip3 install psycopg2-binary')
    #     #     # postgres APP 사용 경우
    #     #     # os.system('sudo ln -s /Applications/Postgres.app/Contents/Versions/9.4/lib/libpq.5.dylib /usr/lib')
    #     finally:
    #         print('module change')
    from API.db.database import engine

    from sqlalchemy import Table, Column, String, ForeignKey
    from sqlalchemy import MetaData



    '''
    create table list
    1. userdata
    2. user_list
    '''

    # metadata
    meta = MetaData()

    userdata = Table(
        'userdata', meta,
        Column('word', String, primary_key=True),
        Column('meaning', String, unique=False),
        # foreign Key
        Column('user', String, ForeignKey("user_list.user"), unique=False)
    )

    User_list = Table(
        'user_list', meta,
        Column('user', String, primary_key=True),
        Column('passwd', String, unique=False)
    )

    # Table create
    conn = engine.connect()
    # with engine.connect as conn:
    #     meta.create_all(conn, checkfirst=False)

