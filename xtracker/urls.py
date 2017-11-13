"""xtracker URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


def home(request):  # view function
    assert False, "BOOM!!!!"

def hello(request, name):  # view function
    return HttpResponse("hello {}!".format(name))

def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(f"{a} + {b} = {c}")

def age(request, name, i):
    x = int(i) + 1
    return HttpResponse(f"{name} is {x} years old.")

# /plus/10/20/
# 10 + 20 = 30

# /age/danny/20/
# /age/20/danny/

urlpatterns = [
    url(r'^$', home),
    url(r'^plus/([0-9]+)/([0-9]+)/$', add),
    url(r'^hello/(\w+)/$', hello),

    # url(r'^age/(\w+)/([0-9]+)/$', age),

    url(r'^age/(?P<i>[0-9]+)/(?P<name>\w+)/$', age),
    url(r'^age/(?P<name>\w+)/(?P<i>[0-9]+)/$', age),

    url(r'^age/(?P<name>\w+)/$', age, kwargs={'i': 16}),

    # url(r'^hello/(udi)/$', hello),
    # url(r'^hello/(yaniv)/$', hello),
    # url(r'^admin/', admin.site.urls),
]
