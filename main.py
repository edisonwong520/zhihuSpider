"""
zhihu web spider

"""
import json
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import random
import traceback
from logger import log_writer
from mongo import insert_mongo, init_mongo
import re
from utils import *
from settings import *
from bson.json_util import dumps

os.system("mkdir -p ./data")


# get zhihu comment
def get_comment(que_id, asw_id):
    tmp = header
    tmp['referer'] = 'https://www.zhihu.com/question/{}'.format(que_id)
    url = "https://www.zhihu.com/api/v4/answers/{}/root_comments?order=normal&limit=20&offset=0&status=open".format(
        asw_id)
    rsp = request_get(url, tmp, {})
    # print(json.dumps(rsp))
    return rsp


#
# def decode_str(s):
#     return s.encode('utf-8').decode("unicode_escape")

#
# def test_get_question(qid):
#     options = webdriver.ChromeOptions()
#     chromedriver_path = "/tmp/chromedriver"
#     options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     # options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
#
#     url = 'https://www.zhihu.com/question/{}'.format(qid)
#     log_writer.debug("get question url {}".format(url))
#     browser.get(url)
#     time.sleep(1)
#     # get all answer
#     temp_height = 0
#     log_writer.debug("start to get scroll")
#     while True:
#         # 循环将滚动条下拉
#         browser.execute_script("window.scrollBy(0,1000)")
#         # sleep一下让滚动条反应一下
#         time.sleep(1)
#         # 获取当前滚动条距离顶部的距离
#         check_height = browser.execute_script(
#             "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
#         # 如果两者相等说明到底了
#         if check_height == temp_height:
#             log_writer.debug("end to get scroll")
#             break
#         temp_height = check_height


def get_question(qid):
    log_writer.debug("start to get qid:{}".format(qid))
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", chromedebug_url)
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    url = 'https://www.zhihu.com/question/{}'.format(qid)
    log_writer.debug("get question url {}".format(url))
    browser.get(url)
    time.sleep(2)
    answer_set = []
    while True:
        # 翻页
        browser.find_element_by_css_selector("body").send_keys(Keys.SPACE)
        browser.find_element_by_css_selector("body").send_keys(Keys.SPACE)
        browser.find_element_by_css_selector("body").send_keys(Keys.SPACE)
        browser.find_element_by_css_selector("body").send_keys(Keys.SPACE)
        # sleep一下让滚动条反应一下
        # time.sleep(0.2)

        cm_data = {}
        le = len(browser.find_elements_by_class_name('List-item'))
        # get each answer
        for num in range(le - 1, 0, -1):
            try:
                answer_dict = {}

                i = browser.find_element_by_xpath(
                    '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[{}]/div/div'.format(num))

                data = json.loads(i.get_attribute("data-za-extra-module"))
                answer_dict = {
                    "questionID": qid,
                    "user": json.loads(i.get_attribute("data-zop"))['authorName'],
                    "thumbsupNum": data["card"]["content"]["upvote_num"],
                    "commentNum": data["card"]["content"]["comment_num"],
                    "publishTimestamp": "{}".format(
                        i.find_element_by_class_name('ContentItem-time').find_element_by_tag_name('span').get_attribute(
                            'data-tooltip')).
                        replace("发布于 ", "", -1),
                    "context": i.find_element_by_class_name('RichContent-inner').text,
                    "picNum": len(i.find_element_by_class_name('RichContent-inner').find_elements_by_tag_name('img')),
                }
                key = "{}{}".format(answer_dict["user"], answer_dict["publishTimestamp"])

                # 如果存在，那就不用往下解析了
                if key in answer_set:
                    break
                else:
                    log_writer.debug("get num answer {}".format(num))
                    answer_set.append(key)
                # 获取评论接口不确定有没有限速/反爬，还是sleep一下吧
                t = random.uniform(0.5, 1)
                item_id = json.loads(i.get_attribute("data-zop"))['itemId']
                log_writer.debug("sleep {}s to get comment , question id:{} , answerid:{}".format(t, qid, item_id))
                time.sleep(t)
                cm_data = get_comment(qid, item_id)
                # log_writer.debug(json.dumps(cm_data))
                comment_list = []
                highlight_comment_list = []

                # travel comment
                for d in cm_data["data"]:
                    c = {
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(d["created_time"]))),
                        'author': str(d["author"]["member"]["name"]),
                        'context': str(d["content"])
                    }
                    if d["featured"]:
                        # time.strftime('%Y-%m-%d %H:%M:%S',x)
                        highlight_comment_list.append(c)
                    else:
                        # 取前10条普通评论
                        if len(comment_list) < 10:
                            comment_list.append(c)
                        else:
                            break
                answer_dict["highlight_comment"] = highlight_comment_list
                answer_dict["comment"] = comment_list
                try:
                    answer_dict["videos"] = len(i.find_element_by_class_name('RichText-video'))
                except Exception as e:
                    pass

                # 存mongo
                insert_mongo(mongo_db_name, mongo_db_table, answer_dict)
                # log_writer.debug(json.dumps(answer_dict, ensure_ascii=False))
            except Exception as e:
                log_writer.error(
                    "get {} answer err {} , data:{} , comment data:{}".format(num, e, answer_dict, cm_data))
                log_writer.error(traceback.format_exc())


#
# def testMongo():
#     # m= init_mongo(MongoDB , "test")
#     insert_mongo(mongo_db_name, "test", {"hello": "yes"})


#
# def testScroll():
#     test_get_question(468847258)

def main():
    for i in question_id_list:
        get_question(i)
        time.sleep(100)


def dump_data():
    options = webdriver.ChromeOptions()

    options.add_experimental_option("debuggerAddress", chromedebug_url)
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    for qid in question_id_list:
        url = 'https://www.zhihu.com/question/{}'.format(qid)
        log_writer.debug("get question url {}".format(url))
        browser.get(url)
        time.sleep(3)
        e = browser.find_element_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[1]/h4/span')
        question_dict = {
            "answerNum": re.compile(r'.\d*').findall("{}".format(e.text).replace(",", "", -1))[0],
            "title": browser.find_element_by_xpath(
                '//*[@id="root"]/div/main/div/div[1]/div[2]/div/div[1]/div[1]/h1').text,
            "questonID": qid,
        }

        col = init_mongo(mongo_db_name, mongo_db_table)

        with open("./data/tmp.json", "w")as file:
            ans = list(col.find({"questionID": qid}))
            file.write(dumps(ans, indent=2))
        with open("./data/tmp.json", "r")as file:
            d = json.load(file)
        with open("./data/{}.json".format(qid), "w") as file2:
            json.dump({
                "question": question_dict,
                "answers": d
            }, file2, ensure_ascii=False)


import csv


def dump_to_excel():
    for qid in question_id_list:
        with open("./data/{}.csv".format(qid), "w", encoding='utf-8-sig') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(
                ["user", "thumbsupNum", "commentNum", "publishTimestamp", "context", "picNum", "videoNum",
                 "highlight_user",
                 "highlight_tm", "highlight_comment", "comment_user", "comment_tm", "comment"])
            with open("./data/{}.json".format(qid), "r")as file:
                d = json.load(file)
            for i in d["answers"]:
                data = [i["user"], i["thumbsupNum"], i["commentNum"], i["publishTimestamp"], i["context"], i["picNum"],
                        0]
                max_count = max(len(i["highlight_comment"]), len(i["comment"]))
                for num in range(max_count):
                    try:
                        if num >= 1:
                            data = ["" for i in range(7)]
                        data += [i["highlight_comment"][num]["author"], i["highlight_comment"][num]["timestamp"],
                                 i["highlight_comment"][num]["context"]]
                    except Exception as e:
                        data += ["" for i in range(3)]
                    try:
                        data += [i["comment"][num]["author"], i["comment"][num]["timestamp"],
                                 i["comment"][num]["context"]]
                    except Exception as e:
                        pass
                    csv_write.writerow(data)


if __name__ == '__main__':
    log_writer.debug("main start")
    dump_to_excel()
    log_writer.debug("main end")
