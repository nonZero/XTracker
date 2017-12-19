from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.home, name='list'),
    path("as-json/", views.home_json, name='list_json'),
    path("add/", views.create, name='create'),
    path("(P<id>[0-9]+)/", views.detail, name='detail'),
    # url(r"^(?P<id>[0-9]+)/comment/", views.create_comment, name='create_comment'),
]
