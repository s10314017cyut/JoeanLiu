from django.conf.urls import url
from weapon import views

urlpatterns = [
               url(r'^$', views.weapon, name='weapon'),
               ]