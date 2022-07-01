import os
import pymysql
from pymysql import cursors

DB_Connect = None


class Storage:
    """
    storage 基础类
    """
    db_connect = None

    def __init__(self):
        global DB_Connect
        DB_HOST = os.getenv("DB_HOST", "")
        DB_PORT = os.getenv("DB_PORT", 0)
        DB_USER = os.getenv("DB_USER", "")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "")
        DB_NAME = os.getenv("DB_NAME", "")
        if not DB_Connect:
            DB_Connect = pymysql.connect(host=DB_HOST,
                                         port=int(DB_PORT),
                                         user=DB_USER,
                                         password=DB_PASSWORD,
                                         database=DB_NAME,
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)
        self.db_connect = DB_Connect
