import json
import math
import os
import time

from src.tools.mysql_connect import MysqlConnect

current_dir = os.path.dirname(__file__)
business_file_dir = os.path.dirname(os.path.dirname(current_dir))
business_file = open(business_file_dir + '/resources/yelp/yelp_academic_dataset_business.json', encoding='utf8')

mysql_connect = MysqlConnect()

con = mysql_connect.get_connect()
cursor = con.cursor()


def insert_business(business):
    try:
        sql = "INSERT INTO yelp.business(`business_id`, `name`, `address`, `city`, `state`, `postal_code`, `latitude`, " \
              "`longitude`, `stars`, `review_count`, `is_open`, `attributes`, `categories`, `hours`) VALUES (%s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

        cursor.execute(sql, (business['business_id'], business['name'], business['address'], business['city'],
                             business['state'], business['postal_code'], business['latitude'], business['longitude'],
                             business['stars'], business['review_count'], business['is_open'], business['attributes'],
                             business['categories'], business['hours']))

        con.commit()
    except Exception as e:
        print('insert error:', e)


start_time = time.time()
print('start time: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
count = 0
for line in business_file.readlines():

    business_item = json.loads(line)
    keys = []
    if business_item['attributes']:
        keys = business_item['attributes'].keys()
    key_values = ''
    for key in keys:
        state = 0
        if business_item['attributes'][key] and business_item['attributes'][key] != 'False':
            state = 1
        key_values += key + ":" + state.__str__() + ","
    hour_keys = []
    if business_item['hours']:
        hour_keys = business_item['hours'].keys()
    hours_str = ''
    for key in hour_keys:
        hours_str += key + ':' + business_item['hours'][key] + ","

    business_item['attributes'] = key_values[0:-1]
    business_item['hours'] = hours_str[0:-1]
    insert_business(business_item)
    count = (1 + count) % 1000
    if count is 0:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '; insert: ' + business_item['business_id'] + '; success!')

end_time = time.time()
print('end time: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print('duration: ' + math.ceil(end_time - start_time))

business_file.close()
