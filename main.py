import pymysql
from config import host, password, db_name

try:
    connection = pymysql.connect(
    host = host,
    port=3306,
    password = password,
    database = db_name,
    cursorclass = pymysql.cursors.DictCursor
    )
    print("successfully connected...")
except Exception as ex:
    print("Connection refused...")
    print(ex)
