import json
import os
import time

from src.tools.mysql_connect import MysqlConnect

current_dir = os.path.dirname(__file__)
user_file_dir = os.path.dirname(os.path.dirname(current_dir))
user_file = open(user_file_dir + '/resources/yelp/yelp_academic_dataset_user.json', encoding='utf8')

mysql_connect = MysqlConnect()
con = mysql_connect.get_connect()
cursor = con.cursor()


def insert_user(user):
    try:
        sql = "INSERT INTO yelp.users(`user_id`, `name`, `review_count`, `yelping_since`, `useful`, `funny`, `cool`, " \
              "`elite`, `friends`, `fans` , `average_stars`, `compliment_hot`, `compliment_more`, " \
              "`compliment_profile`, `compliment_list`, `compliment_note`, `compliment_plain`, `compliment_cool`, " \
              "`compliment_funny`, `compliment_writer`, `compliment_photos`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

        cursor.execute(sql, (user['user_id'], user['name'], user['review_count'], user['yelping_since'], user['useful'],
                             user['funny'], user['cool'], user['elite'], user['friends'], user['fans'],
                             user['average_stars'], user['compliment_hot'], user['compliment_more'],
                             user['compliment_profile'], user['compliment_list'], user['compliment_note'],
                             user['compliment_plain'], user['compliment_cool'], user['compliment_funny'],
                             user['compliment_writer'], user['compliment_photos']))

        con.commit()
    except Exception as e:
        print('insert error:', e)
    print(time.time().__str__() + '; insert: ' + user['user_id'] + '; success!')


for line in user_file.readlines():
    user = json.loads(line)
    insert_user(user)

user_file.close()
