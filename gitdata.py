import pymysql
import json

# 从一个数据表中，拉下所有合适的数据，所以需要提供一个数据表(两个)
# 调试的时候，需要按日期选择数据，所以日期会有一个时间戳范围
# 所选的数据被储存到本地，那么需要一个文件名（文件名即可记录当前的运行参数）

table_name1 = "data_21074"  # 初级侧单片机的数据表
table_name2 = "data_21074"  # 次级侧单片机的数据表
time_stamp_begin = "2010-03-01 00:00:00"
time_stamp_end = "2020-03-01 00:00:00"
filename1 = "fuck.json"
filename2 = "test2.json"

# 连接数据库
db = pymysql.connect(host = 'cdb-i98x3ehb.gz.tencentcdb.com',
                    user='root',
                    password='84711p38',
                    db='615power',
                    charset='utf8mb4',
                    port = 10136,
                    cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

sql_get_manager = "select * from " + "db_manager"

cursor.execute(sql_get_manager)

results = cursor.fetchall()

print(results[0]['id_string'])
print(results)


# 将给定表指定时间的数据拉下来
def store_data(cursor, table_name, filename, time_stamp_begin, time_stamp_end):
    # 预定义表结构
    sql_get_data = "select * from " + table_name
    cursor.execute(sql_get_data)
    results = cursor.fetchall()

    fp = open(filename, 'w')
    json.dump(results, fp)
    fp.close()


store_data(cursor, table_name1, filename1, time_stamp_begin, time_stamp_end)



# +--------------------------+-------+------+------------+---------+
# | id_string                | id    | type | table_name | next_id |
# +--------------------------+-------+------+------------+---------+
# | manager                  |     0 |   99 | manager    |   21075 |
# | hifgdebchifgdebchifgdebc |     1 | 1280 | data_1     |   21025 |
# | eipphjaghiiefefdbhfdbgib | 21074 |    1 | data_21074 |    NULL |
# +--------------------------+-------+------+------------+---------|

# sprintf(query_statement, "create table %s (ch0_max float,ch0_min float,ch0_ave float,ch0_var float,ch0_index_min smallint,\
#   ch0_index_max smallint,ch1_max float,ch1_min float,ch1_ave float,ch1_var float, ch1_index_min smallint,\
#   ch1_index_max smallint,ch2_max float,ch2_min float,ch2_ave float,ch2_var float, ch2_index_min smallint, \
#   ch2_index_max smallint,ch3_max float,ch3_min float,ch3_ave float,ch3_var float, ch3_index_min smallint, \
#   ch3_index_max smallint,ch4_max float,ch4_min float,ch4_ave float,ch4_var float, ch4_index_min smallint, \
#   ch4_index_max smallint,ch5_max float,ch5_min float,ch5_ave float,ch5_var float, ch5_index_min smallint, \
#   ch5_index_max smallint,ch6_max float,ch6_min float,ch6_ave float,ch6_var float, ch6_index_min smallint, \
#   ch6_index_max smallint,sample_rate int,boost_freq int,llc_freq int,tmp float,timer smallint,count smallint);",
#         table_name);


db.close()