from django.conf.urls import url
from AH import views


urlpatterns = [
               url(r'^$', views.AH, name='AH'),
]