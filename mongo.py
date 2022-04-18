from pymongo import MongoClient
import time
import pymongo
import traceback
from settings import *


# 初始化mongo
def init_mongo(db_name, table_name):
    db = MongoClient(mongo_ip, int(mongo_port))[db_name]
    db.authenticate(mongo_user, mongo_password)
    mongo_collection = db[table_name]
    return mongo_collection


# obj id 转化为时间戳
def parse_time(object_id):
    time_stamp = int(object_id[:8], 16)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))


from logger import log_writer


def get_mongo_docs(db_name, table_name, id):
    mongo_col = init_mongo(db_name, table_name)
    return int(mongo_col.count_documents({"questionID": id}))


# 插入mongo
def insert_mongo(db_name, table_name, data):
    # setup_logger(log_name)
    # log_writer = log.getLogger(log_name)
    mongo_col = init_mongo(db_name, table_name)
    before_count = int(mongo_col.count_documents({}))
    insert_flag = False
    try:
        if type(data) == type([]):
            mongo_col.insert_many(data, ordered=False)
        elif type(data) == type({}):
            mongo_col.insert_one(data)
        insert_flag = True
    # except pymongo.errors
    except pymongo.errors.DuplicateKeyError as e:
        log_writer.info(
            "insert mongo duplicate error,db_name : {},db_table :{} , data:{}".format(db_name, table_name, e, data))
    except Exception as e:
        log_writer.error("insert mongo error,db_name : {},db_table :{}".format(db_name, table_name, e))
        log_writer.error(traceback.format_exc())

    after_count = int(mongo_col.count_documents({}))
    if insert_flag:
        log_writer.info(
            "insert success , after insert mongo , db_name:{} , table_name:{} ,data count:{} , insert data num: {}".format(
                db_name, table_name,
                after_count, after_count - before_count))
    return {"before_count": before_count, "after_count": after_count}

#
# # 获取处理后的最后一条记录的_id
# def get_last_doc(db_name, table_name, reverse=False):
#     mongo_col = init_mongo(db_name, table_name)
#     if reverse:
#         result = mongo_col.find().sort([("_id", -1)]).limit(1)
#         for doc in result:
#             return dict(doc)
#     else:
#         result = mongo_col.find().sort([("_id", 1)]).limit(1)
#         for doc in result:
#             return dict(doc)
#     return {}


#
# if __name__ == "__main__":
#     print(parse_time("5dcefba7763fd92b81fe7fc4"))
