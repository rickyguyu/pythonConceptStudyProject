import random

from django.http import HttpResponse
from django.shortcuts import render
from .models import UserInfo
# Create your views here.

def toLogin_view(request):
    return render(request,"login.html")

def login_view(request):
    u = request.POST.get("user","")
    p = request.POST.get("pwd","")
    if u and p:
        c = UserInfo.objects.filter(user_name=u,user_pwd=p).count()
        if c==1:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("用户名或密码错误")
    else:
        return HttpResponse("请输入用户名和密码")

def toregister_view(request):
    return render(request,"registry.html")

def register_view(request):
    u = request.POST.get("user", "")
    p = request.POST.get("pwd", "")
    if u and p:
        user = UserInfo(id=str(random.randrange(0000,9999)),user_name=u,user_pwd=p)
        user.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入用户名和密码")



