from apscheduler.scheduler import Scheduler
import requests
import json

GLOBAL_WEIXIN_TOKEN = ""
GLOBAL_WEIXIN_TICKET = ""

task = Scheduler()

@task.interval_schedule(seconds=0)
def startTask():
    print("后台任务开始")
    task.shutdown(wait=False)
    getWeiXinToken()
    createTask()
task.start()


def createTask():
    sc = Scheduler()
    sc.add_interval_job(getWeiXinToken, seconds=60*60)
    sc.start()


def getWeiXinToken():
    s = requests.Session()
    appid = "wxeb9d7c0a2c777790"
    secret = "d5ee8bdfa4dda203c03ade14215a5d15"
    address = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&" \
              "appid="+appid+"&secret="+secret;
    result = s.get(address, verify=False)
    code = result.status_code
    if code == 200:
        print("请求微信token返回", result.content)
        content = json.loads(result.content)
        global GLOBAL_WEIXIN_TOKEN
        GLOBAL_WEIXIN_TOKEN = content["access_token"]
        print(GLOBAL_WEIXIN_TOKEN)
        getWeiXinTicket(GLOBAL_WEIXIN_TOKEN)
    else:
        print("获取微信token识别 result code is ", result.status_code + result.content)


def getWeiXinTicket(token):
    s = requests.Session()
    address = "http://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&" \
              "access_token="+token;
    result = s.get(address, verify=False)
    code = result.status_code
    if code == 200:
        print("请求微信 js ticket 返回", result.content)
        content = json.loads(result.content)
        global GLOBAL_WEIXIN_TICKET
        GLOBAL_WEIXIN_TICKET = content["ticket"];
        print(GLOBAL_WEIXIN_TICKET)
    else:
        print("请求微信 js ticket ", result.status_code + result.content)





