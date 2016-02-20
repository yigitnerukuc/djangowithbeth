from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.beth, name='index'),
    url(r'^beth/', views.beth, name='beth'),
    url(r'^yigit/', views.yigit, name='yigit'),
]