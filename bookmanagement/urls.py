"""bookmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as login_view


def include(param):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', login_view.index),
    path(r'login/', login_view.login),
    path(r'register/', login_view.register),
    path(r'handle_register/', login_view.handle_register),
    path(r'literature/', login_view.literature),
    path(r'science/', login_view.science),
    path(r'comic/', login_view.comic),
    path(r'novel/', login_view.novel),
    path(r'blog/', login_view.blog),
    path(r'contact/', login_view.contact),
    path(r'/contact/', login_view.contact),
    path(r'/', login_view.index),
    path(r'/literature/', login_view.literature),
    path(r'/science/', login_view.science),
    path(r'/comic/', login_view.comic),
    path(r'/novel/', login_view.novel),
    path(r'/login/', login_view.login),
    path(r'/register/', login_view.register),
    #path(r'login/blog/',login_view.blog)
]
