#coding=utf-8
from django.shortcuts import render
from models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'user_info/index.html')
def login(request):
    return render(request, 'user_info/login.html')


def register(request):
    return render(request, 'user_info/register.html')
def register_handle(request):
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    if pwd != cpwd:
        return redirect('/register/')
    udata = UserInfo.users.create(user_name, pwd, email)
    udata.save()
    return redirect('/login/')
def register_exist(request):
    uname = request.GET.get('uname')
    num = UserInfo.users.filter(uName=uname).count()
    return JsonResponse({'count': num})

def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title':'用户登录', 'error_name':0, 'error_pwd':0, 'uname':uname}
    return render(request, 'user_info/login.html', context)
def login_handle(request):
    info = request.POST
    uname = info.get('username')
    upwd = info.get('pwd')
    jizhu = info.get('jizhu', 0)
    user = UserInfo.users.filter(uName=uname)
    # 后台校验
    # if len(user) == 0:
    #    return redirect('/login/')
    # else:
    #   if user[0].uName == uname and user[0].uPasswd == upwd:
    #        return redirect('/index/')
    #   else:
    #        return redirect('/login/')

    # 前台校验
    if len(user) == 1:
        if upwd == user[0].uPasswd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            red.set_cookie('url', '', max_age=-1)
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'用户登录', 'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd':upwd}
            return render(request, 'user_info/login.html', context)
    else:
        context = {'title':'用户登录', 'error_name':1, 'error_pwd':0, 'uname':uname, 'upwd':upwd}
        return render(request, 'user_info/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')