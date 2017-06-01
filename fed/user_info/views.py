#coding=utf-8
from django.shortcuts import render
from models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import user_decorator
# Create your views here.

def index(request):
    return render(request, 'user_info/index.html')

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
            # 获取cookie,key为url,不存在时默认为'/'
            url = request.COOKIES.get('url', '/')
            # 生成一个HttpResponseRedirect对象,用于模拟一个用户的请求
            red = HttpResponseRedirect(url)
            # 成功后删除转向地址,防止以后直接登录造成的转向
            red.set_cookie('url', '', max_age=-1)
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                # max_age -1表示关闭浏览器就过期
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

@user_decorator.login
def ucenter_info(request):
    user_email = UserInfo.users.get(id=request.session['user_id']).uEmail
    # 最近浏览
    goods_list=[]
    goods_ids=request.COOKIES.get('goods_ids','')
    if goods_ids!='':
        goods_ids1=goods_ids.split(',')#['']
        GoodsInfo.objects.filter(id__in=goods_ids1)
        for goods_id in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['user_name'],
        'page_name': 1,
        'goodlist': goods_list,
    }
    return render(request, 'user_info/user_center_info.html', context)

@user_decorator.login
def ucenter_site(request):
    user = UserInfo.users.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.uShou = post.get('uname')
        user.uAddr = post.get('uaddr')
        user.uTel = post.get('utel')
        user.uYoubian = post.get('uyoubian')
        user.save()
    context = {
        'title': '用户中心',
        'user': user,
        'page_num': 1,
    }
    return render(request, 'user_info/user_center_site.html', context)