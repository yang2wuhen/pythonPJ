"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *

from oa.api.wechat import *
from oa.views.login import *
from oa.views.wechat import *


# ----------------------用于后台定时任务不能删除----------------------
from apscheduler.scheduler import Scheduler
from oa.tasks import startTask
# -----------------------后台定时任务配置完成-------------------------


urlpatterns = [
    url('^loginAction/$', loginResult),
    url('^login/$', login),

    url('^callback/$', callback),  # 微信回调接口

    # 微信登录界面
    url('^index/$',index),

]