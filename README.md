## 介绍
知乎爬虫：爬指定问题的所有答案（包括点赞数、图片数、评论数），以及每一个答案下的精选评论、普通评论  

A web spider which can grep all the answers,comments and thumb up numbers etc... of a specific question in Zhihu.  

仅供学习交流，严禁用于商业用途，请于24小时内删除

## 环境
- Python3 , 安装requirements.txt依赖
- Mac OS Big Sur，别的系统也可以，需要下载对应版本的chrome driver即可
- mongoDB，别的数据库也可以，自行改造即可（不选mysql是因为python sql还需要声明model太费劲，字段longtext长度可能不够，以及python orm对比gorm太难用了。。。）建议加上按 【问题-用户名-时间戳】作唯一索引，防止插入重复数据

## 用法
- 改settings.py里的配置
- 手动在mac终端执行```/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=9222  --user-data-dir="/tmp/ChromeProfile"``` 启动chrome，别的系统可自行google
- 在新的chrome里登陆自己的知乎账号
- python3 main.py 执行代码
- 爬到自己满意的数据，然后手动结束脚本

## 执行结果
mongo里的数据，例：
```angular2html
{
    "_id" : "",
    "questionID" : 282620628,
    "user" : "xx",
    "thumbsupNum" : 18,
    "commentNum" : 11,
    "publishTimestamp" : "2019-07-31 10:50",
    "context" : "后悔，不是说我失败了...",
    "picNum" : 6,
    "highlight_comment" : [],
    "comment" : [ 
        {
            "timestamp" : "2019-08-02 13:31:56",
            "author" : "xx",
            "context" : "<p>虽然整后的照片还行...</p>"
        }
    ]
}
```

## 思路
- debug启动chrome，python脚本attach 到chrome（本来想用golang 写的，但似乎golang selenium库没有attach remote debug url功能）
- selenium，模拟不断按空格往下滑，解析html
- 性能：100条回答大概花了5分钟
- 其他：知乎反爬还是做的不错的。一开始想的是用api，结果发现api是动态加密header头的，懒得研究js代码里加密逻辑了。遂转用selenium，selenium启动的chrome估计是因为带有特殊user agent 之类的header头被知乎解析到并禁止爬虫。后面改成先手动起debug chrome，然后代码attach过去。期间发现评论的接口没有动态加密，所以可以用普通的get请求获取。

## TODO
 - 改成headless 浏览器（节省渲染的时间），代码自动登陆知乎，而不是手动登陆 
 - 改成并发爬取，优化爬取速度
 - 现在是手动结束，之前试过判断页面高度与scroll bar 高度，当滑动到最底不能再滑动的时候，两个高度应该是相等的。但这个会有问题，就是中间页面会卡住，其实还能往下滑的。所以改成死循环，靠人手动停止
 - 支持断点，从上次爬的位置继续爬，现在如果中间网络抖动啥的断开，那就悲剧了-。-