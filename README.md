
# 主要功能
    1. 中国白银网 7*24小时快讯、白银资讯、行业白银资讯 爬取,解析,存储
# 主要技术
    bs4
    xpath
    celery
    requests
    mongodb
    redis
    简要流程: 通过ajax 获取数据（id和其他），通过id 获取html， 解析html和ajax 获取的数据，redis缓存数据，mongodb存储数据
# 测试环境
    install:
        virtualenv
        python3+
        inrequirements.txt
    /db/init_database.py    配置测试数据库
    /page_parse/qiniu_deal.py   环境变量配置七牛云的key和空间
    /db/conf.py 配置celery redis
    celery -A tasks.workers worker -B -Q new,info,trade_info -l info

# 生产环境
    编译Dockerfile,运行docker容器(需要配置七牛云的key和空间)
# 代码说明
    /config     配置资讯和requests请求相关信息

    /db         初始化 redis、mongodb,定义mongodb 表结构和相关表操作方法

    /logger     配置存储日志和日志格式

    /page_get   资讯 list 和content 获取(ajax)
        news.py         7*24小时快讯
        info.py         白银资讯
        trade_info.py   行业白银资讯
    /page_parse 资讯 list 和content 解析 和七牛储存图片(docker构建传入key和空间)

    /tasks      celery 配置，7*24小时快讯、白银资讯、行业白银资讯 task（主要传递数据和存储数据）

    /tests      目前未加测试（数据的获取和解析 /page_get 和/page_parse 里面的文件可单独测试）