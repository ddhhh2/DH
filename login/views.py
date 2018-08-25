from django.shortcuts import render, redirect
from login.models import User
from login.login_decorator import is_login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')
        message = "！"
        if useremail and userpassword:  # 确保用户名和密码都不为空
            email = useremail.strip()

            try:
                user = User.objects.get(useremail=email)
                if user.password == userpassword:
                    user_status=request.set_cookie("user_status",useremail)

                    return redirect('/blog/')
                else:
                    message = "Password Error！"
                    return message
            except:
                message = "Email Error！"
                return message
        return render(request, 'Login.html', {"message": message})
    return render(request, "Login.html")


def register(request):
    return render(request, "register.html")


def handle_register(request):
    useremail = request.POST.get("email")
    userpassword = request.POST.get("password")

    user = User()
    user.email = useremail
    user.password = userpassword
    user.create()

    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        message = "请检查填写的内容！"


def literature(request):
    return render(request, "Literature.html")


def science(request):
    return render(request, "science.html")


def comic(request):
    return render(request, "comic.html")


def novel(request):
    return render(request, "Novel.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")
