import pymysql

SQL_HOST = 'localhost'
SQL_USER = 'duncte123'
SQL_PASS = ''
SQL_DB = 'sayai'

connection = pymysql.connect(host=SQL_HOST,
                             user=SQL_USER,
                             password=SQL_PASS,
                             db=SQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_saying(saying):
    if not connection.open:
        print("Reconnecting to database")
        connection.ping(reconnect=True)

    with connection.cursor() as cursor:
        # Create a new record
        # language=MariaDB
        sql = "INSERT INTO `sayings` (`SayingText`, `SayingDate`) VALUES (%s, CURRENT_DATE())"
        cursor.execute(sql, saying)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
