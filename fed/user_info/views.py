from django.shortcuts import render
from models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
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
    print num
    print '-------------'
    return JsonResponse({'count': num})

def login(request):
    return render(request, 'user_info/login.html')
def login_handle(request):
    info = request.POST
    uname = info.get('user_name')
    npwd = info.get('pwd')
    
