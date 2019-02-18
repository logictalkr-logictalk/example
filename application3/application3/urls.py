from django.conf.urls import url
from application3 import views

app_name = 'application3'

urlpatterns = [
    url(r'^$', views.home,name = 'home'),
    url(r'^reg$',views.reg,name='reg'),
    url(r'^login$',views.login,name = 'login'),


]