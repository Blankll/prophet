import mysql.connector
from settings import db_settings


class MysqlConnect(object):
    def __init__(self):
        self.con = mysql.connector.connect(
            host=db_settings['HOST'],
            port=db_settings['PORT'],
            user=db_settings['USER'],
            password=db_settings['PASSWORD'],
            db=db_settings['DB'],
            charset='utf8',
        )

    def get_connect(self):
        return self.con

    def get_cursor(self):
        return self.cursor()
