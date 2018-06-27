from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'regapp'

urlpatterns = [
	url(r'^$', views.RegView, name = 'index'),
]
