import pymysql

from config.sql import SQL_HOST, SQL_USER, SQL_PASS, SQL_DB

connection = pymysql.connect(host=SQL_HOST,
                             user=SQL_USER,
                             password=SQL_PASS,
                             db=SQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
connection.close()


def insert_saying(saying):
    try:
        if not connection.open:
            connection.ping(reconnect=True)

        with connection.cursor() as cursor:
            # Create a new record
            # language=MariaDB
            sql = "INSERT INTO `sayings` (`SayingText`, `SayingDate`) VALUES (%s, CURRENT_DATE())"
            cursor.execute(sql, saying)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
