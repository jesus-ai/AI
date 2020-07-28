import pymysql

from config.sql import SQL_HOST, SQL_USER, SQL_PASS, SQL_DB

if SQL_HOST is not None:
    connection = pymysql.connect(host=SQL_HOST,
                                 user=SQL_USER,
                                 password=SQL_PASS,
                                 db=SQL_DB,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    connection.close()


def insert_sayings(sayings, db_name='sayings'):
    try:
        if not connection.open:
            connection.ping(reconnect=True)

        with connection.cursor() as cursor:
            # Create a new record
            for saying in sayings:
                # language=MariaDB
                sql = f"INSERT INTO `{db_name}` (`SayingText`, `SayingDate`) VALUES (%s, CURRENT_DATE())"
                cursor.execute(sql, saying)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
