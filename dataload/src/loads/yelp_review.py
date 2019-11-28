import json
import os
import time

from src.tools.mysql_connect import MysqlConnect

current_dir = os.path.dirname(__file__)
review_file_dir = os.path.dirname(os.path.dirname(current_dir))
review_file = open(review_file_dir + '/resources/yelp/yelp_academic_dataset_review.json', encoding='utf8')

mysql_connect = MysqlConnect()
con = mysql_connect.get_connect()
cursor = con.cursor()


def insert_review(review):
    try:
        sql = "INSERT INTO yelp.reviews(`review_id`, `user_id`, `business_id`, `stars`, `useful`, `funny`, `cool`, " \
              "`text`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        cursor.execute(sql, (review['review_id'], review['user_id'], review['business_id'], review['stars'], review['useful'], review['funny'], review['cool'], review['text'], review['date']))
    except Exception as e:
        print('insert error:', e)


count = 0
for line in review_file.readlines():
    count = (1 + count) % 1000
    insert_review(json.loads(line))
    if count is 0:
        try:
            con.commit()
        except Exception as e:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert commit failure!')
            print(e)
            exit()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert success!')

review_file.close()
