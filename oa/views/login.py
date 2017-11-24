from oa.models import UserInfoModel
from django.shortcuts import render
from django.http import HttpResponse
from oa.utils.session import Session

import logging
logger = logging.getLogger("wechat.views")


def login(request):
    return render(request, 'login.html')


def loginResult (request):
    name = request.POST["name"]
    pwd = request.POST["pwd"]
    if str(name).strip() == "":
        logger.warning("用户名为空")
    elif str(pwd).strip() == "":
        logger.warning("密码为空")
    else:
        try:
            user = UserInfoModel.objects.get(userName=name)
        except UserInfoModel.DoesNotExist:
            logger.warning("用户不存在")
        else:
            logger.info("用户查找成功")
            request.session["session"] = Session().createSession(name, pwd)
            return render(request, "home.html", {"user": user})
    return render(request, "login.html")


def logonOut(request):
    del request.session["session"]
    return HttpResponse('logout ok!')
