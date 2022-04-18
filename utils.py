import json
import requests


def request_get(url, headers, data):
    # data_s = json.dumps(data)
    rsp_str = requests.get(url, headers=headers, json=data).text
    try:
        json_result = json.loads(rsp_str)
        return json_result
    except Exception as _e:
        print("parse json error: url is {}".format(url))
        return {}


def request_post(url, headers, data):
    # data_s = json.dumps(data)
    rsp_str = requests.post(url, headers=headers, json=data).text
    try:
        json_result = json.loads(rsp_str)
        return json_result
    except Exception as _e:
        print("parse json error: url is {}".format(url))
        return {}


def request_post_data(url, headers, data):
    # data_s = json.dumps(data)
    rsp_str = requests.post(url, headers=headers, data=data).text
    try:
        json_result = json.loads(rsp_str)
        return json_result
    except Exception as _e:
        print("parse json error: url is {}".format(url))
        return {}


def request_post_html(url, headers, data):
    # data_s = json.dumps(data)
    return requests.post(url, headers=headers, json=data).text


def request_put(url, headers, data):
    # data_s = json.dumps(data)
    rsp_str = requests.put(url, headers=headers, json=data).text
    try:
        json_result = json.loads(rsp_str)
        return json_result
    except Exception as _e:
        print("parse json error: url is {}".format(url))
        return {}


def request_put_html(url, headers, data):
    return requests.put(url, headers=headers, json=data).text


def request_delete(url, headers, data):
    rsp_str = requests.delete(url=url, headers=headers, json=data).text
    try:
        json_result = json.loads(rsp_str)
        return json_result
    except Exception as _e:
        print("parse json error: url is {}".format(url))
        return {}


def request_delete_html(url, headers, data):
    return requests.delete(url=url, headers=headers, json=data).text
