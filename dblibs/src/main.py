import logging

import sqlalchemy
from sqlalchemy import create_engine, text

logging.basicConfig(format="'%(asctime)s' %(name)s : %(message)s'", level=logging.INFO)
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)
logger = logging.getLogger('main')

# Tutorial - https://docs.sqlalchemy.org/en/20/tutorial/index.html

if __name__ == '__main__':
    logger.info('Version = {}'.format(sqlalchemy.__version__))

    engine = create_engine('sqlite:///:memory:', future=True)

    # The default behavior of the Python DBAPI includes that a transaction is always in progress; when the scope of the connection is released, a ROLLBACK is emitted to end
    # the transaction. The transaction is not committed automatically; when we want to commit data we normally need to call Connection.commit()
    # DBAPI connection is non-autocommitting
    with engine.connect() as conn:
        sql = "select 'hello world'"
        result = conn.execute(text(sql))

        # it’s best to ensure "Result" object is consumed within the “connect” block, and is not passed along outside of the scope of our connection
        all_results = result.all()
        logger.info('Output for "{}" = {}'.format(sql, all_results))

    # "commit as you go"
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )

        # Commit inside the block where we acquired the Connection object. After we call this method inside the block, we can continue to run more SQL statements and if we
        # choose we may call Connection.commit() again for subsequent statements. SQLAlchemy refers to this style as commit as you go.
        conn.commit()

    # "begin once"
    # everything inside of a begin() block will be auto-COMMITed at the end, assuming a successful block, or ROLLBACK in case of exception raise
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
        )

    # executing an ORM session (which os equivalent to core's connection) : https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#executing-with-an-orm-session
