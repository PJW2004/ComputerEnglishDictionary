from API.db.database import engine

from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy import MetaData

if __name__ == "__main__":
    meta = MetaData()

    testtable = Table(
        'testtable', meta,
        Column('test', String, primary_key=True)
    )

    conn = engine.connect()