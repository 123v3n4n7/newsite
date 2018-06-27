from django.urls import path
from django.conf.urls import url
from . import views

from rest_framework.authtoken import views as vm

app_name = 'loginsys'

urlpatterns = [
	url(r'^login/$', views.login2, name = 'login2'),
	url(r'^logout/$', views.logout, name = 'logout'),
	url(r'^registration/$', views.registration, name = 'registration'),
	url(r'^users/$', views.UserCreate.as_view(), name = 'account-create'),
	
	url(r'^registr/$', views.RegisterUser.as_view(), name = 'reg'),
	
	url(r'^log2/$', views.ObtainAuthToken.as_view(), name = 'log2'),
	url(r'^profile/$', views.ProfileListView, name = 'profile'),
] 
