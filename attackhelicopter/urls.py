from django.conf.urls import url
from attackhelicopter import views

urlpatterns = [
               url(r'^$', views.attackhelicopter, name='attackhelicopter'),
]