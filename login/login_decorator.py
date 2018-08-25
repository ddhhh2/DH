from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def is_login(func):
    # *args 表示传入的参数为列表或者元组，其中列表可以被改变，元组不可以被改变数值
    # **kwargs 表示传入的参数为字典
    def login_func(request,*args,**kwargs):
        if request.COOKIE.has_key("user_status"):
            return func(request,*args,**kwargs)
        else:
            return redirect("/")


    return login_func


#@login
#def comment():
#    print("11111")

if __name__ == '__main__':
    comment()