mongo_ip = "127.0.0.1"
mongo_user = "zhihuSpider"
mongo_password = "z0mpJL1z1d9t6"
mongo_port = "27017"
mongo_db_name = "zhihuSpider"
mongo_db_table = "zhihuSpider"

chromedriver_path = "/tmp/chromedriver"
chromedebug_url = "127.0.0.1:9222"

# 可以手动从知乎网页获取header，header 主要用于调用评论接口 eg：https://www.zhihu.com/api/v4/answers/{}/root_comments?order=normal&limit=20&offset=0&status=open
header = {
    'authority': 'www.zhihu.com',
    'x-zse-93': '101_3_2.0',
    'x-ab-param': 'tp_topic_style=0;tp_dingyue_video=0;zr_expslotpaid=6;pf_adjust=1;qap_question_author=0;tp_zrec=1;top_test_4_liguangyi=1;qap_question_visitor= 0;pf_noti_entry_num=2;tp_contents=1;zr_slotpaidexp=1;se_ffzx_jushen1=0',
    'x-ab-pb': 'CroBKgThBPMDdQTaBNYENAxgC58CcgP0AzsCUAO0ADcFQwBVBcEEMgX2AkUEVgW0CqADzATPC9wLPwBHAAsE6QSJDOALjALoA0IE0QQ0BOMEGQVSBUABKgKiAzMENwx0AcwCCgQyA30CZAQHDGkBoQO5AvcDVgzsCscCVwM/BVEFAQuEAlILFAUpBZsL4AQRBRUF5Aq3A1cEMwX0C9cC2AKmBA8LtQv4A2wEygIOBRIFGwBPA2oBjgPXC2wDEl0AAgAAAQEAAAEBAAAAAAEVAAAAAAEAAAABCwAAAAABAAAAAAAFAAEABAEAAAABAAABAAEBAQIAFQEBAQAIAAAAAAECAAABAAIAAAECAAAAAAEDAQAAAAAAAAABAAE=',
    'x-zst-81': '3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YD_02XtucXYqK6P0E79y-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Io4cpr4w0mRPO7HoY70SfquPmz93mhDQyiqV9ebO1hwOYiiR0ELYuUrxmtDomqU7ynXtOnAoTh_PhRDSTFMC9FCX14CXCUrLyFGpBegCyzUVy9CLGnG2f8cSm2wVqZgxmtwp_o4N1_92TvMx9SwgO6hSfDhFCiwLmbvHO1goGp9tmDbN_Z92BZvwLthcV9qO0TBeVbXVOHggBoqXKiBOpZUC9p7XGeJS0ACLGEcLOEDXLWrrVDUt1ZUgC8AN_8CXmCqkw99CGdrNLn9SCk8c_2GgKNupMbqgq-JS__USfcgcfsGOMicPshBXfngpGkq3_e8Oxk7p1hD3qVUOZ2_pVFbS1-DpfqrXOIuw9bug1sTHq8hVMQXHMWBLC',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'x-app-version': '6.42.0',
    'sec-ch-ua-mobile': '?0',
    'x-requested-with': 'fetch',
    'x-zse-96': '2.0_aTN8ND98SR2Ye72qK_tynDuyNhOxUhS0KLtynv90k8Ox',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zhihu.com/question/34436105',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_zap=9d6035bd-f784-48ce-854a-5c9c8b1833cc; _xsrf=he9bryvQcLAjxIjapHAtHzLje6O1Fy34; d_c0="AKAf5Uls0BOPToLZffTpeDiT_rWfFyy8REc=|1633184545"; __snaker__id=1kOZ5LoXi4Qsk6ru; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=UfxLKC9bdUf4ePEUwDNWe1JOWKW66hoPzfVNcUrDypCGVfqgDPU2aw%2FRT%2FAhU2McE1fgQfVoK80RI%2BmVsCIhWGYfMKvmtZ8LnRRjO4v1tA6pkUT6CvTZ%2FifARJbL5ZuFb3Q%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb3b1399af5fbd5eb33f6b88fb6d54a839f9fafaa80919a8cadc56396b8bfd7d52af0fea7c3b92a97bab8adca49fbbeacb6e540a7908bb6f6508e89abd2c945959599d7b564ad90b687d546a18bbea5fc7c81999a87f46d88909bd3e47ded8e9cd0c46497ee8384c83ba6b99f87d56589e800b3cc21af8abda4cc6495999787d041b6b3bcbbbb48ae8e9e8bce40b6efbca2b57ca98b9cd7c27e9886e18ae54b9296aeadb852b79aaed4d437e2a3; YD00517437729195%3AWM_TID=P0BIQcgY%2FAFABAVARBZrsXVCeAnA0%2BvV; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1633184545,1633228102,1633236506; r_cap_id="2|1:0|10:1633243192|8:r_cap_id|44:ODQ3YzYyZWY1NTk3NDBlMDk3ZGI4MGY3MjEyNzM1MmU=|6e5987d33681a5fcd3fe8d0eebdd31eed8d8871a60833ba8b039372a4df48833"; gdxidpyhxdE=7gyIzgugH0Ry4VHC4TnRXTBAAByZ%2B4oQDGgJctJG0x7X71SuuG1f6RrHLe9en0R5QfTf0RxYNwB9YHur962SGWM5SGnM1Usy6dSwJ4yjGEJQTJi90Q1IdMlf3jHmhpRa8pxW8H%2BmOz%2FfZ2E2Rq5iPSd4UWZeQQ0q0U9gRfCzo9qKiB0S%3A1633244097945; captcha_session_v2="2|1:0|10:1633243201|18:captcha_session_v2|88:cURJeFZZSUVHek1DZTVwQ29paU12WEJ2Q0ZBY1Rrbmw1cmtNZ1hBdXBJVUhYandVRXE4YXZzdHJxdStQMDJmWA==|4d3c98cee49ebaea8731cab6f7be0099d71b1f54200f48a949db0185c5b33e67"; captcha_ticket_v2="2|1:0|10:1633243207|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfUWZwdkpYeXJkeDJoVE1CWURPSDQ4OWVwaEp5ZTVqcUlIRmNYRHpBTnFjRWY4V3AyVlgyVHRyN0Q1Ulk2eXktYUlnYTExR0hYVDhMYnlnYktOTXdOazk2WlFoRFh3VHdxeXM1djdkUFBWcTZ6VlpRZHR5VmZ5a1lzUUFPYkJMbHc3ZFZfTmNJNy5LcFZVdXVCeVZXdHlaZlVERmhQWmRtdk5yWFdsTTk4azZpeW93XzhabncuYnpmWkNBVGVvcEhHQ21TNHNaY3VJbk5jeDRScUFuWS0uLWt0X3psMWQ2OGc5eWZ4dTlHNGFCNGxnMUhlRXVadi1NZ19fWlU3WGUtR3h6RS5CZU0wTzJxNVBTNnk2QTVHQ1NBLV90UVN2NWM2LmlDeHNZVUtfbi5wZ0l6MlpBMEU4MVpZaGliRU9KMVNXZlhpbkV2YVkuV1guTFNUd2FOeGFMVWFUMFR5T3oxYWk2d1plZWVPQ0p4OWxRWHoxa1ZsYVctZnc1X2U0YjVLbmFDMEpvRUtISkF5MUNWVG56Z0VvTC5VbmFzR0NMdkJfTTFyWG9aWU9HdXFCazdwX29QOVhPeGpoaFhha202bmJtZzkweXRTcVhkS1c3dWMwbVEuNW01NWdxSm1oRzlVSnBmSHBkeVdnOUJ0SFI2UVFWTWp6NHVvSFJpMyJ9|564cd8b629d42752c261efe8329c972488a29af9c460a0b69d2b7ecda9ce8f7f"; z_c0="2|1:0|10:1633243208|4:z_c0|92:Mi4xVTBZd0FBQUFBQUFBb0JfbFNXelFFeVlBQUFCZ0FsVk5TSjVHWWdCYlUyNC15WkxjU0pLSTJkQkplaDBFdEFZSFZn|2206dc668d48863ba3ef5af1c8ba2b1ed2a2ae33b3ca6ce0f39e74b4802e96dd"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1633243883; KLBRSID=3d7feb8a094c905a519e532f6843365f|1633243931|1633236505',
}

# 写上你想获取的question id ，eg：https://www.zhihu.com/question/282620628
question_id_list = [34436105, ]
# question_id_list = [34436105, 348357205, 27470291, 337211885, 282620628, 31947726]
