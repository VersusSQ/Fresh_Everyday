#coding=utf-8
from django.http import HttpResponseRedirect

# 如果没有登录,则跳转到登录界面
def login(func):
    def login_in(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            # 重定向
            red = HttpResponseRedirect('/login/')
            # 设置url的cookie
            red.set_cookie('url', request.get_full_path())
            return red
    return login_in


# http://127.0.0.1:8080/200/?type=10
# request.path：表示当前路径，为/200/
# request.get_full_path()：表示完整路径，为/200/?type=10