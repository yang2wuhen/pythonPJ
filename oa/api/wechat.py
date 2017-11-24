from django.shortcuts import render
from django.http import HttpResponse

import requests, json

accessToken = ""
refreshToken = ""
openid = ""


def callback(request):
    appid = "wxeb9d7c0a2c777790"
    secret = "d5ee8bdfa4dda203c03ade14215a5d15"
    code = request.GET.get("code")
    state = request.GET.get("state")
    if code is not None:
        address = "https://api.weixin.qq.com/sns/oauth2/access_token?appid="+appid+"&" \
                    "secret="+secret+"&code="+code+"&grant_type=authorization_code"
        result = requests.session().get(address, verify=True)
        code = result.status_code
        if code == 200:
            print("请求微信授权token", result.content)
            content = json.loads(result.content)
            accessToke = content["access_token"]
            openid = content["openid"]
            refreshToken = content["refresh_token"]
            if accessToke is not None:
                address = "https://api.weixin.qq.com/sns/userinfo?access_token" \
                          "="+accessToke+"&openid="+openid+"&lang=zh_CN"
                result = requests.session().get(address, verify=True)
                code = result.status_code
                if code == 200:
                    print("请求访问用户信息", result.content)
                    return render(request, "wechat/index.html",
                                  {"userinfo": json.loads(result.content)})
                    # return HttpResponse(result.content)
                else:
                    return HttpResponse("获取用户信息失败")
        else:
            return HttpResponse("请求微信授权token失败")
    else:
        return HttpResponse("微信回调失败")







