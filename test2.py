import json
import numpy

table_name1 = "data_21074"  # 初级侧单片机的数据表
table_name2 = "data_21074"  # 次级侧单片机的数据表
time_stamp_begin = "2010-03-01 00:00:00"
time_stamp_end = "2020-03-01 00:00:00"
filename1 = "fuck.json"
filename2 = "test2.json"

fp = open(filename1, 'r')
data = json.load(fp)

def json2list(data):
    rawlist = list()

    key = list(data[0].keys())
    print(key)

    for raw in data:
        value = list(raw.values())
        rawlist.append(value)

    return rawlist


matrix = numpy.array(json2list(data), dtype=numpy.float32)
print(matrix.T)