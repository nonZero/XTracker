from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    url(r"^$", views.home, name='list'),
    url(r"^add/$", views.create, name='create'),
    url(r"^(?P<id>[0-9]+)/$", views.detail, name='detail'),
    url(r"^(?P<id>[0-9]+)/comment/$", views.create_comment, name='create_comment'),
]
