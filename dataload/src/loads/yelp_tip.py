import json
import os
import time

from src.tools.mysql_connect import MysqlConnect

current_dir = os.path.dirname(__file__)
tip_file_dir = os.path.dirname(os.path.dirname(current_dir))
tip_file = open(tip_file_dir + '/resources/yelp/yelp_academic_dataset_tip.json', encoding='utf8')

mysql_connect = MysqlConnect()
con = mysql_connect.get_connect()
cursor = con.cursor()


def insert_tip(tip):
    try:
        sql = "INSERT INTO yelp.tips(`user_id`, `business_id`, `text`, `date`, `compliment_count`) VALUES (%s, %s, " \
              "%s, %s, %s) "
        cursor.execute(sql, (tip['user_id'], tip['business_id'], tip['text'], tip['date'], tip['compliment_count']))
    except Exception as e:
        print('insert error:', e)


count = 0
for line in tip_file.readlines():
    insert_tip(json.loads(line))
    count = (1 + count) % 1000
    if count is 0:
        try:
            con.commit()
        except Exception as e:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert commit failure!')
            print(e)
            exit()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert success!')

tip_file.close()
