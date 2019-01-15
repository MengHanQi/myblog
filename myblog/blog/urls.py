from django.urls import path
from . import views

urlpatterns = [
    path(r'^index/$', views.index),
    path(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
]
