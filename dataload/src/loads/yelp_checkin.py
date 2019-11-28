import json
import os
import time

from src.tools.mysql_connect import MysqlConnect

current_dir = os.path.dirname(__file__)
checkin_file_dir = os.path.dirname(os.path.dirname(current_dir))
checkin_file = open(checkin_file_dir + '/resources/yelp/yelp_academic_dataset_checkin.json', encoding='utf8')

mysql_connect = MysqlConnect()
con = mysql_connect.get_connect()
cursor = con.cursor()


def insert_checkin(checkin):
    try:
        sql = "INSERT INTO yelp.checkins(`business_id`, `date`) VALUES (%s, %s) "
        date = checkin['date'].split(',')
        for date_item in date:
            cursor.execute(sql, (checkin['business_id'], date_item))
    except Exception as e:
        print('insert error:', e)


count = 0
for line in checkin_file.readlines():
    count = (1 + count) % 1000
    insert_checkin(json.loads(line))
    if count is 0:
        try:
            con.commit()
        except Exception as e:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert commit failure!')
            print(e)
            exit()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert success!')

checkin_file.close()
