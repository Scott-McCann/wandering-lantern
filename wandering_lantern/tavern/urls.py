from django.conf.urls import url
import views

url(r'^$', views.tavern_index, name='index' )
